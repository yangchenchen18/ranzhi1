import sys,os
sys.path.append(os.getcwd())
import unittest
from page.login_page import LoginPage
from base.util import BoxDriver
from parameterized import parameterized
from base.util import GetExcle,GetLogger




class LoginTest(unittest.TestCase):

    def setUp(self):
        # driver = BoxDriver()
        # self.page = LoginPage(driver)
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(self):
        self.driver = BoxDriver()
        self.page = LoginPage(self.driver)
        self.logger=GetLogger('ranzhi.log')
        self.logger.info('打开浏览器')
    @classmethod
    def tearDownClass(self):
        # self.driver = BoxDriver()
        # self.page = LoginPage(self.driver)
        self.driver.quit()

    # for uname, upwd in [('admin','123456'),('tom','123456'),('user0','123456')]:
    #     test_login_success(uname,upwd)
    # 用例参数化
    @parameterized.expand(GetExcle().GetExcle(r'.\config\data.xlsx','login_success'))
    def test_login_success(self,uname,upwd,realname1):
        '''登陆成功功能测试用例'''
        try:
            page = self.page
            page.login(uname,upwd)
            self.logger=GetLogger('ranzhi.log')
            self.logger.info('登录完成')
            # 断言
            realname2 = page.get_real_name()
            self.assertEqual(realname1,realname2,'登陆成功测试用例失败！')
            self.logger=GetLogger('ranzhi.log')
            self.logger.info('断言成功')
        except:
            raise NameError('输入名字有误')
        finally:
            page.logout()
            self.logger=GetLogger('ranzhi.log')
            self.logger.info('签退')
        # # page.login('tom','123456')
        # # # 断言
        # realname = page.get_real_name()
        # self.assertEqual(realname,'admin','登陆成功测试用例失败！')
        # page.logout()

    @parameterized.expand(GetExcle().GetExcle(r'.\config\data.xlsx','login_fail'))
    def test_login_fail(self,uname,upwd):
        '''登陆失败功能测试用例'''
        page = self.page
        page.login(uname,upwd)
        
        # 断言
        confim=page.get_confim()
        self.assertEqual(confim,'确认','登录失败测试用例失败')
        page.confim()

if __name__ == "__main__":
    unittest.main()