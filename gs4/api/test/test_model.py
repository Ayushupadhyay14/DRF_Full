from django.test import TestCase
from .models import Account


class AccountModelTest(TestCase):

    def setUp(self):
        self.account = Account.objects.create(
            user="Ayush",
            account_name="Personal Account",
            created="2025-08-23"
        )

    def test_account_creation(self):
        """Check if account object is created correctly"""
        self.assertEqual(self.account.user, "Ayush")
        self.assertEqual(self.account.account_name, "Personal Account")
        self.assertEqual(self.account.created, "2025-08-23")

    def test_account_str_method(self):
        """Check the string representation of Account"""
        expected_str = "Personal Account (Ayush)"
        self.assertEqual(str(self.account), expected_str)

    def test_update_account(self):
        """Check if account can be updated"""
        self.account.account_name = "Updated Account"
        self.account.save()
        self.assertEqual(self.account.account_name, "Updated Account")

    def test_delete_account(self):
        """Check if account deletion works"""
        account_id = self.account.id
        self.account.delete()
        self.assertFalse(Account.objects.filter(id=account_id).exists())
