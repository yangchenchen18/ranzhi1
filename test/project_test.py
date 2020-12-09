import sys,os
sys.path.append(os.getcwd())
from page.login_page import LoginPage
from page.addproject_page import AddProject
from base.util import BoxDriver,GetExcle
import unittest
from parameterized import parameterized

class Project_test(unittest.TestCase):
    def setUp(self):
        pass
    @classmethod
    def setUpClass(self):
        '''打开浏览器登录、添加项目
        '''
        self.driver=BoxDriver()
        self.project=AddProject(self.driver)
        self.project.login()
        self.project.add_pro()
    @classmethod
    def tearDownClass(self):
        pass
    @parameterized.expand(GetExcle().GetExcle(r'./config/data.xlsx','project'))
    def test_add_project(self,title,num):
        '''添加项目测试用例成功'''
        project=self.project
        self.project.add_qk()
        project.add_project(title,num)
        # 断言
        account=project.get_pname()
        self.assertEqual(account,title,'添加项目测试用例成功')
        
        


if __name__ == "__main__":
    unittest.main()
