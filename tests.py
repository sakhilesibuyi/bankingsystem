from django.test import TestCase

from api.models import (
    Account,
    AccountType,
    Bank,
    Branch,
    Client,
    ClientConsultant,
    Deposit,
    Transfer,
    Withdrawal
)

#Test if branch creation works
class BranchTestCase(TestCase):
    def setUp(self):
        #Branch.objects.create(branch_name="Midrand - Boulders",branch_code="23456988")
        #Branch.objects.create(branch_name="Midrand - Carlswald",branch_code="8596231")
        self.branch = Branch.objects.create(
            branch_name="Midrand - Boulders",
            branch_code="23456988"
        )
    def test_branches_exists(self):
        self.assertEqual(self.branch,"Midrand - Boulders")
    
    
