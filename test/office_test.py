import sys,os
sys.path.append(os.getcwd())
from page.office_page import AddOffice
from page.login_page import LoginPage
from base.util import BoxDriver,GetExcle
from parameterized import parameterized
import unittest

class OfficeTest(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass
        # self.driver.close()
    @classmethod
    def setUpClass(self):
        self.driver=BoxDriver()
        self.office=AddOffice(self.driver)
        self.office.login()
        self.office.switch_frame()
    @classmethod
    def tearDownClass(self):
        pass
    @parameterized.expand(GetExcle().GetExcle(r'./config/data.xlsx','office'))
    def test_office_success(self,title,num):
        '''添加系统或者日历'''
        office=self.office
        office.add_off()
        office.add_office(title,num)
        # 断言
        accout=office.get_pname()
        self.assertEqual(accout,title,'添加日历或系统用例测试成功')
if __name__ == "__main__":
    unittest.main()

