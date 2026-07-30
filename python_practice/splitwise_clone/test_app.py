import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(__file__))

import app as splitwise_app
from models import db, Expense, ExpenseSplit, Group, GroupMember, Settlement, User


class SplitwiseAppTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_uri = splitwise_app.Config.SQLALCHEMY_DATABASE_URI
        splitwise_app.Config.SQLALCHEMY_DATABASE_URI = (
            f"sqlite:///{os.path.join(self.temp_dir.name, 'test.db')}"
        )

        self.app = splitwise_app.create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

            group = Group(name="Trip")
            alice = User(name="Alice")
            bob = User(name="Bob")
            db.session.add_all([group, alice, bob])
            db.session.commit()

            db.session.add_all(
                [
                    GroupMember(group_id=group.id, user_id=alice.id),
                    GroupMember(group_id=group.id, user_id=bob.id),
                ]
            )
            db.session.commit()

            self.group_id = group.id
            self.alice_id = alice.id
            self.bob_id = bob.id

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
            db.engine.dispose()

        splitwise_app.Config.SQLALCHEMY_DATABASE_URI = self.original_uri
        self.temp_dir.cleanup()

    def test_invalid_unequal_split_does_not_persist_expense(self):
        response = self.client.post(
            "/expenses",
            json={
                "group_id": self.group_id,
                "amount": 100,
                "paid_by": self.alice_id,
                "split_mode": "unequal",
                "splits": [
                    {"user_id": self.alice_id, "amount": 30},
                    {"user_id": self.bob_id, "amount": 50},
                ],
            },
        )

        self.assertEqual(response.status_code, 400)

        with self.app.app_context():
            self.assertEqual(Expense.query.count(), 0)
            self.assertEqual(ExpenseSplit.query.count(), 0)

    def test_settle_becomes_noop_once_group_is_settled(self):
        create_expense = self.client.post(
            "/expenses",
            json={
                "group_id": self.group_id,
                "amount": 100,
                "paid_by": self.alice_id,
                "split_mode": "equal",
                "split_between": [self.alice_id, self.bob_id],
            },
        )
        self.assertEqual(create_expense.status_code, 201)

        first_settle = self.client.post("/settle", json={"group_id": self.group_id})
        self.assertEqual(first_settle.status_code, 200)
        self.assertEqual(len(first_settle.get_json()), 1)

        second_settle = self.client.post("/settle", json={"group_id": self.group_id})
        self.assertEqual(second_settle.status_code, 200)
        self.assertEqual(second_settle.get_json(), [])

        with self.app.app_context():
            self.assertEqual(Settlement.query.count(), 1)

    def test_member_can_be_removed_after_settled_balance(self):
        create_expense = self.client.post(
            "/expenses",
            json={
                "group_id": self.group_id,
                "amount": 100,
                "paid_by": self.alice_id,
                "split_mode": "equal",
                "split_between": [self.alice_id, self.bob_id],
            },
        )
        self.assertEqual(create_expense.status_code, 201)

        settle_response = self.client.post("/settle", json={"group_id": self.group_id})
        self.assertEqual(settle_response.status_code, 200)

        remove_response = self.client.delete(
            f"/groups/{self.group_id}/members/{self.bob_id}"
        )
        self.assertEqual(remove_response.status_code, 200)

        with self.app.app_context():
            self.assertIsNone(
                GroupMember.query.filter_by(
                    group_id=self.group_id, user_id=self.bob_id
                ).first()
            )


if __name__ == "__main__":
    unittest.main()
