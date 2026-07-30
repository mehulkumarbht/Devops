import os
import runpy
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(__file__))

import app as splitwise_app
from models import db, Expense, ExpenseSplit, Group, GroupMember, Settlement, User


class SeedScriptTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_uri = splitwise_app.Config.SQLALCHEMY_DATABASE_URI
        splitwise_app.Config.SQLALCHEMY_DATABASE_URI = (
            f"sqlite:///{os.path.join(self.temp_dir.name, 'seed.db')}"
        )
        self.app = splitwise_app.create_app()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.engine.dispose()

        splitwise_app.Config.SQLALCHEMY_DATABASE_URI = self.original_uri
        self.temp_dir.cleanup()

    def test_seed_script_is_idempotent(self):
        seed_path = os.path.join(os.path.dirname(__file__), "seed.py")

        runpy.run_path(seed_path, run_name="__main__")
        runpy.run_path(seed_path, run_name="__main__")

        with self.app.app_context():
            self.assertEqual(User.query.count(), 3)
            self.assertEqual(Group.query.count(), 1)
            self.assertEqual(GroupMember.query.count(), 3)
            self.assertEqual(Expense.query.count(), 1)
            self.assertEqual(ExpenseSplit.query.count(), 3)
            self.assertEqual(Settlement.query.count(), 0)


if __name__ == "__main__":
    unittest.main()
