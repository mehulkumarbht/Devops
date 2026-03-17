from app import create_app, db
from app import User, Group, GroupMember, Expense, ExpenseSplit

app = create_app()

with app.app_context():
    db.create_all()

    u1 = User(name="Mehul")
    u2 = User(name="Alice")
    u3 = User(name="Bob")
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
