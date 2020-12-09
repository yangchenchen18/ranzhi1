
import sys,os
sys.path.append(os.getcwd())
from page.addteam_page import AddTeam
import unittest
from page.login_page import LoginPage
from base.util import BoxDriver
from parameterized import parameterized
from base.util import GetExcle


class AddTeamTest(unittest.TestCase):


    def setUp(self):
        pass
    def tearDown(self):
        pass
    @classmethod
    def setUpClass(self):
        pass
    @classmethod
    def tearDownClass(self):
        pass
    @parameterized.expand(GetExcle().GetExcle(r'.\config\data.xlsx','team'))
    def test_addteam_success(self,title,num):
        self.driver = BoxDriver()
        addTeam = AddTeam(self.driver)
        addTeam.login()
        addTeam.addteam(title,num)
if __name__ == "__main__":
    unittest.main()
        

