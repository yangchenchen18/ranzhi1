import sys,os
sys.path.append(os.getcwd())
from page.login_page import LoginPage
import unittest
from page.addmoney_page import AddMoney
from base.util import BoxDriver,BasePage,GetExcle,GetLogger
from parameterized import parameterized


class Addmoney_test(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        self.driver=BoxDriver()
        self.addmoney=AddMoney(self.driver)
        self.addmoney.login()
        self.addmoney.switch_frame()
        self.logger=GetLogger("ranzhi1.log")
        self.logger.info("打开浏览器并登录成功")



    @classmethod    
    def tearDownClass(self):
        driver=self.driver
        driver.close()
        self.logger=GetLogger("ranzhi1.log")
        self.logger.info("关闭浏览器")
    @parameterized.expand((GetExcle().GetExcle(r'./config/data.xlsx','office')))
    def test_money_success(self,title,num):
        '''现金记账用例添加成功'''
        addmoney=self.addmoney
        addmoney.add_qk()
        addmoney.add_money(title,num)
        acc=addmoney.get_mname()
        self.logger=GetLogger("ranzhi1.log")
        self.logger.info("3条用例添加成功")
        # self.assertEquals(acc,accout1,"现金记账添加用例成功")
        # self.logger.info("断言成功")
        
    
        
        
        
        

if __name__ == "__main__":
    unittest.main()
    
