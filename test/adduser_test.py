
import sys,os
sys.path.append(os.getcwd())

from base.util import BoxDriver,BasePage,GetExcle
import unittest
from page.login_page import LoginPage
from page.adduser_page import AddUser
from parameterized import parameterized
class AddUserTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):    
        self.driver = BoxDriver()
        self.adduser = AddUser(self.driver)
        self.adduser.login()
        self.adduser.add_u()
    #  adduser = self.adduser
    @parameterized.expand(GetExcle().GetExcle(r'./config/data.xlsx','user'))
    def test_adduser(self,username,password):
    
        ''''添加用户测试用例成功'''
        self.adduser.add_user(username,password)
        # # realname=self.addUser.get_name()
        # # self.assertEqual(realname,username,'真实姓名不一致')
        self.adduser.addnext()
if __name__ == "__main__":
    unittest.main()
