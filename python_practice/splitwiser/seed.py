from app import create_app, db
from app import User, Group, GroupMember, Expense, ExpenseSplit, Settlement

app = create_app()


def reset_seed_data():
    db.session.query(ExpenseSplit).delete(synchronize_session=False)
    db.session.query(Settlement).delete(synchronize_session=False)
    db.session.query(Expense).delete(synchronize_session=False)
    db.session.query(GroupMember).delete(synchronize_session=False)
    db.session.query(Group).delete(synchronize_session=False)
    db.session.query(User).delete(synchronize_session=False)
    db.session.commit()


with app.app_context():
    try:
        db.create_all()
        reset_seed_data()

        u1 = User(name="Mehul").ensure_credentials(
            username="mehul", password="Password1"
        )
        u2 = User(name="Alice").ensure_credentials(
            username="alice", password="Password1"
        )
        u3 = User(name="Bob").ensure_credentials(username="bob", password="Password1")
        db.session.add_all([u1, u2, u3])
        db.session.commit()

        g = Group(name="Test Group")
        db.session.add(g)
        db.session.commit()

        db.session.add_all(
            [
                GroupMember(group_id=g.id, user_id=u1.id),
                GroupMember(group_id=g.id, user_id=u2.id),
                GroupMember(group_id=g.id, user_id=u3.id),
            ]
        )
        db.session.commit()

        e = Expense(group_id=g.id, description="Dinner", amount=300, paid_by=u1.id)
        db.session.add(e)
        db.session.commit()

        db.session.add_all(
            [
                ExpenseSplit(expense_id=e.id, user_id=u1.id, share_amount=100),
                ExpenseSplit(expense_id=e.id, user_id=u2.id, share_amount=100),
                ExpenseSplit(expense_id=e.id, user_id=u3.id, share_amount=100),
            ]
        )
        db.session.commit()

        print("Database seeded successfully.")
    finally:
        db.session.remove()
        db.engine.dispose()
