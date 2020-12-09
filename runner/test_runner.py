# import sys,os
# sys.path.append(os.getcwd())
import sys,os
sys.path.append(os.getcwd())
import unittest
from base.HTMLTestRunner import HTMLTestRunner
import time
from base.util import SendMail
class TestRunner:

    def runner(self):
        # 实例化测试套件，可以看做一个容器
        # 把部分用例挑选出来，加载到容器中执行
        suite = unittest.TestSuite()
        # 加载用例,可以用通配符匹配
        suite.addTests(unittest.TestLoader().discover('./test/',pattern='addmoney_test.py'))
        # 创建HTML报告文件
        timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
        path='./report/report_%s.html'%timestamp
        report = open(path,mode='wb')
        # 创建用例运行器，用于运行用例并生成报告
        test_runner = HTMLTestRunner(stream=report,title='ranzhi自动化测试报告',description='报告的详细内容描述......')
        # 运行用例
        test_runner.run(suite)
        # 将报告发送到邮件中
        SendMail().sendmail('ranzhi自动化测试报告',path)
        


if __name__ == "__main__":
    TestRunner().runner()