from collections import defaultdict
from flask import Flask, jsonify, render_template, request
from config import Config
from models import db, User, Group, GroupMember, Expense, ExpenseSplit, Settlement


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    def calculate_balances(group_id):
        balances = defaultdict(lambda: defaultdict(float))
        expenses = Expense.query.filter_by(group_id=group_id).all()

        for expense in expenses:
            payer = expense.paid_by
            for split in expense.splits:
                if split.user_id is None:
                    continue
                if split.user_id != payer:
                    balances[split.user_id][payer] += float(split.share_amount)

        return balances

    def simplify_balances(group_id):
        net_balance = defaultdict(float)

        member_ids = [
            gm.user_id for gm in GroupMember.query.filter_by(group_id=group_id).all()
        ]
        member_ids_set = set(member_ids)

        expenses = Expense.query.filter_by(group_id=group_id).all()
        for expense in expenses:
            if expense.paid_by not in member_ids_set:
                continue

            for split in expense.splits:
                if split.user_id is None or split.user_id not in member_ids_set:
                    continue

                share = round(float(split.share_amount), 2)
                net_balance[split.user_id] -= share
                net_balance[expense.paid_by] += share

        settlements = Settlement.query.filter_by(group_id=group_id).all()
        for s in settlements:
            if s.from_user_id in member_ids_set:
                net_balance[s.from_user_id] += round(float(s.amount), 2)
            if s.to_user_id in member_ids_set:
                net_balance[s.to_user_id] -= round(float(s.amount), 2)

        creditors = []
        debtors = []

        for user_id in member_ids:
            balance = round(net_balance[user_id], 2)
            if balance > 0:
                creditors.append([user_id, balance])
            elif balance < 0:
                debtors.append([user_id, abs(balance)])

        transactions = []
        i = 0
        j = 0

        while i < len(debtors) and j < len(creditors):
            debtor_id, debt = debtors[i]
            creditor_id, credit = creditors[j]

            if debtor_id == creditor_id:
                i += 1
                continue

            amount = round(min(debt, credit), 2)
            if amount <= 0:
                break

            debtor = db.session.get(User, debtor_id)
            creditor = db.session.get(User, creditor_id)

            if not debtor or not creditor:
                if debt <= credit:
                    i += 1
                else:
                    j += 1
                continue

            transactions.append(
                {
                    "from_user_id": debtor_id,
                    "to_user_id": creditor_id,
                    "from_user_name": debtor.name,
                    "to_user_name": creditor.name,
                    "amount": amount,
                }
            )

            debtors[i][1] = round(debtors[i][1] - amount, 2)
            creditors[j][1] = round(creditors[j][1] - amount, 2)

            if debtors[i][1] == 0:
                i += 1
            if creditors[j][1] == 0:
                j += 1

        return transactions

    @app.route("/")
    def home():
        groups = Group.query.all()
        return jsonify(
            {
                "message": "Splitwise Clone Running!",
                "groups": [{"id": g.id, "name": g.name} for g in groups],
            }
        )

    @app.route("/groups/<int:group_id>")
    def group_page(group_id):
        group = db.session.get(Group, group_id)
        if not group:
            return "Group not found", 404
        return render_template("index.html", group_id=group_id)

    @app.route("/groups/<int:group_id>/members")
    def get_group_members(group_id):
        members = (
            db.session.query(User)
            .join(GroupMember, User.id == GroupMember.user_id)
            .filter(GroupMember.group_id == group_id)
            .all()
        )

        return jsonify([{"id": user.id, "name": user.name} for user in members])

    @app.route("/groups/<int:group_id>/balances")
    def get_balances(group_id):
        balances = calculate_balances(group_id)
        result = []

        for debtor, creditors in balances.items():
            for creditor, amount in creditors.items():
                if amount > 0:
                    result.append(
                        {
                            "from_user": debtor,
                            "to_user": creditor,
                            "amount": round(amount, 2),
                        }
                    )

        return jsonify({"balances": result})

    @app.route("/groups/<int:group_id>/summary")
    def group_summary(group_id):
        net_balance = defaultdict(float)

        expenses = Expense.query.filter_by(group_id=group_id).all()
        for expense in expenses:
            for split in expense.splits:
                if split.user_id is None:
                    continue
                net_balance[split.user_id] -= round(float(split.share_amount), 2)
                net_balance[expense.paid_by] += round(float(split.share_amount), 2)

        settlements = Settlement.query.filter_by(group_id=group_id).all()
        for s in settlements:
            net_balance[s.from_user_id] += round(float(s.amount), 2)
            net_balance[s.to_user_id] -= round(float(s.amount), 2)

        member_ids = [
            gm.user_id for gm in GroupMember.query.filter_by(group_id=group_id).all()
        ]

        result = []
        for user_id in member_ids:
            user = db.session.get(User, user_id)
            if not user:
                continue

            balance = round(net_balance[user_id], 2)

            result.append(
                {
                    "user_id": user.id,
                    "user_name": user.name,
                    "balance": balance,
                    "status": "gets back"
                    if balance > 0
                    else "owes"
                    if balance < 0
                    else "settled",
                }
            )

        return jsonify(result)

    @app.route("/expenses", methods=["POST"])
    def add_expense():
        data = request.get_json()

        if not data:
            return {"error": "Invalid JSON"}, 400

        try:
            group_id = int(data["group_id"])
            amount = float(data["amount"])
            paid_by = int(data["paid_by"])
        except (KeyError, TypeError, ValueError):
            return {
                "error": "group_id, amount, and paid_by are required and must be valid"
            }, 400

        description = data.get("description", "")
        split_mode = data.get("split_mode", "equal")

        expense = Expense(
            group_id=group_id,
            description=description,
            amount=amount,
            paid_by=paid_by,
            split_between=None,
        )
        db.session.add(expense)
        db.session.commit()

        if split_mode == "equal":
            split_between = data.get("split_between", [])

            clean_ids = []
            for x in split_between:
                try:
                    clean_ids.append(int(x))
                except (TypeError, ValueError):
                    continue

            clean_ids = list(dict.fromkeys(clean_ids))

            if len(clean_ids) == 0:
                db.session.delete(expense)
                db.session.commit()
                return {
                    "error": "split_between must have at least one valid user ID"
                }, 400

            share = round(amount / len(clean_ids), 2)
            expense.split_between = ",".join(str(x) for x in clean_ids)

            for user_id in clean_ids:
                db.session.add(
                    ExpenseSplit(
                        expense_id=expense.id, user_id=user_id, share_amount=share
                    )
                )

        elif split_mode == "unequal":
            splits = data.get("splits", [])

            if not splits or not isinstance(splits, list):
                db.session.delete(expense)
                db.session.commit()
                return {"error": "splits must be a non-empty list"}, 400

            total_split = 0
            valid_user_ids = []

            for item in splits:
                try:
                    user_id = int(item["user_id"])
                    share_amount = float(item["amount"])
                except (KeyError, TypeError, ValueError):
                    db.session.delete(expense)
                    db.session.commit()
                    return {
                        "error": "Each split must have valid user_id and amount"
                    }, 400

                if share_amount < 0:
                    db.session.delete(expense)
                    db.session.commit()
                    return {"error": "Split amounts cannot be negative"}, 400

                total_split += share_amount
                valid_user_ids.append(user_id)

                db.session.add(
                    ExpenseSplit(
                        expense_id=expense.id,
                        user_id=user_id,
                        share_amount=round(share_amount, 2),
                    )
                )

            if round(total_split, 2) != round(amount, 2):
                db.session.rollback()
                return {
                    "error": "Sum of split amounts must equal total expense amount"
                }, 400

            expense.split_between = ",".join(str(x) for x in valid_user_ids)

        else:
            db.session.delete(expense)
            db.session.commit()
            return {"error": "Invalid split_mode. Use 'equal' or 'unequal'."}, 400

        db.session.commit()
        return {"message": "Expense added successfully", "expense_id": expense.id}, 201

    @app.route("/expenses/<int:expense_id>", methods=["DELETE"])
    def delete_expense(expense_id):
        expense = db.session.get(Expense, expense_id)

        if not expense:
            return {"error": "Expense not found"}, 404

        ExpenseSplit.query.filter_by(expense_id=expense.id).delete()
        db.session.delete(expense)
        db.session.commit()

        return {"message": "Expense deleted successfully"}

    @app.route("/expenses/<int:expense_id>", methods=["PUT"])
    def edit_expense(expense_id):
        expense = db.session.get(Expense, expense_id)

        if not expense:
            return {"error": "Expense not found"}, 404

        data = request.get_json()
        if not data:
            return {"error": "Invalid JSON"}, 400

        try:
            description = data.get("description", expense.description)
            amount = float(data.get("amount", expense.amount))
            paid_by = int(data.get("paid_by", expense.paid_by))
        except (TypeError, ValueError):
            return {"error": "Invalid description/amount/paid_by"}, 400

        split_mode = data.get("split_mode", "equal")

        expense.description = description
        expense.amount = amount
        expense.paid_by = paid_by

        ExpenseSplit.query.filter_by(expense_id=expense.id).delete()

        if split_mode == "equal":
            split_between = data.get("split_between", [])
            clean_ids = []

            for x in split_between:
                try:
                    clean_ids.append(int(x))
                except (TypeError, ValueError):
                    continue

            clean_ids = list(dict.fromkeys(clean_ids))

            if len(clean_ids) == 0:
                return {
                    "error": "split_between must have at least one valid user ID"
                }, 400

            share = round(amount / len(clean_ids), 2)
            expense.split_between = ",".join(str(x) for x in clean_ids)

            for user_id in clean_ids:
                db.session.add(
                    ExpenseSplit(
                        expense_id=expense.id, user_id=user_id, share_amount=share
                    )
                )

        elif split_mode == "unequal":
            splits = data.get("splits", [])

            if not splits or not isinstance(splits, list):
                return {"error": "splits must be a non-empty list"}, 400

            total_split = 0
            valid_user_ids = []

            for item in splits:
                try:
                    user_id = int(item["user_id"])
                    share_amount = float(item["amount"])
                except (KeyError, TypeError, ValueError):
                    return {
                        "error": "Each split must have valid user_id and amount"
                    }, 400

                if share_amount < 0:
                    return {"error": "Split amounts cannot be negative"}, 400

                total_split += share_amount
                valid_user_ids.append(user_id)

                db.session.add(
                    ExpenseSplit(
                        expense_id=expense.id,
                        user_id=user_id,
                        share_amount=round(share_amount, 2),
                    )
                )

            if round(total_split, 2) != round(amount, 2):
                db.session.rollback()
                return {
                    "error": "Sum of split amounts must equal total expense amount"
                }, 400

            expense.split_between = ",".join(str(x) for x in valid_user_ids)

        else:
            return {"error": "Invalid split_mode. Use 'equal' or 'unequal'."}, 400

        db.session.commit()
        return {"message": "Expense updated successfully"}

    @app.route("/settlements/<int:group_id>")
    def get_settlements(group_id):
        transactions = simplify_balances(group_id)
        return jsonify(transactions)

    @app.route("/settle", methods=["POST"])
    def settle():
        data = request.get_json() or {}
        group_id = int(data.get("group_id", 0))
        if not group_id:
            return {"error": "group_id required"}, 400

        Settlement.query.filter_by(group_id=group_id).delete()
        db.session.commit()

        member_ids = [
            gm.user_id for gm in GroupMember.query.filter_by(group_id=group_id).all()
        ]
        member_ids_set = set(member_ids)

        net = defaultdict(float)

        expenses = Expense.query.filter_by(group_id=group_id).all()
        for exp in expenses:
            if exp.paid_by not in member_ids_set:
                continue

            for sp in exp.splits:
                if sp.user_id is None or sp.user_id not in member_ids_set:
                    continue

                share = round(float(sp.share_amount), 2)
                net[sp.user_id] -= share
                net[exp.paid_by] += share

        creditors = []
        debtors = []
        for uid in member_ids:
            bal = round(net[uid], 2)
            if bal > 0:
                creditors.append([uid, bal])
            elif bal < 0:
                debtors.append([uid, abs(bal)])

        suggestions = []
        i = 0
        j = 0

        while i < len(debtors) and j < len(creditors):
            debtor_id, debt = debtors[i]
            creditor_id, credit = creditors[j]

            if debtor_id == creditor_id:
                i += 1
                continue

            amt = round(min(debt, credit), 2)
            if amt <= 0:
                break

            debtor = db.session.get(User, debtor_id)
            creditor = db.session.get(User, creditor_id)

            if not debtor or not creditor:
                if debt <= credit:
                    i += 1
                else:
                    j += 1
                continue

            suggestions.append(
                {
                    "from_user_id": debtor_id,
                    "to_user_id": creditor_id,
                    "from_user_name": debtor.name,
                    "to_user_name": creditor.name,
                    "amount": amt,
                }
            )

            db.session.add(
                Settlement(
                    group_id=group_id,
                    from_user_id=debtor_id,
                    to_user_id=creditor_id,
                    amount=amt,
                )
            )

            debtors[i][1] = round(debtors[i][1] - amt, 2)
            creditors[j][1] = round(creditors[j][1] - amt, 2)

            if debtors[i][1] == 0:
                i += 1
            if creditors[j][1] == 0:
                j += 1

        db.session.commit()
        return jsonify(suggestions)

    @app.route("/history/<int:group_id>")
    def history(group_id):
        expenses = Expense.query.filter_by(group_id=group_id).all()
        settlements = Settlement.query.filter_by(group_id=group_id).all()

        history_items = []

        for e in expenses:
            payer = db.session.get(User, e.paid_by)
            history_items.append(
                {
                    "id": e.id,
                    "type": "expense",
                    "description": e.description,
                    "amount": round(float(e.amount), 2),
                    "paid_by": payer.name if payer else f"User {e.paid_by}",
                    "paid_by_id": e.paid_by,
                    "split_between": e.split_between,
                    "created_at": e.created_at.isoformat() if e.created_at else "",
                }
            )

        for s in settlements:
            from_user = db.session.get(User, s.from_user_id)
            to_user = db.session.get(User, s.to_user_id)

            history_items.append(
                {
                    "id": s.id,
                    "type": "settlement",
                    "amount": round(float(s.amount), 2),
                    "from_user": from_user.name
                    if from_user
                    else f"User {s.from_user_id}",
                    "to_user": to_user.name if to_user else f"User {s.to_user_id}",
                    "created_at": s.created_at.isoformat()
                    if getattr(s, "created_at", None)
                    else "",
                }
            )

        history_items.sort(key=lambda x: x["created_at"], reverse=True)
        return jsonify(history_items)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
