# 单元测试unittest
import unittest
# 必须要继承testcase类
class Test01(unittest.TestCase):
    @classmethod
    def test1(self):
        print('*****这是test1方法*******')
    # @classmethod 注解
    def test2(self):
        print('*****这是test2方法*******')
    # 继承自父类testcase的方法，名字不能乱写
    # setUp方法回自动在每一个测试用例前执行
    @classmethod
    def setUpClass(self):
        print('这是setupclass方法')
    @classmethod
    def tearDownClass(self):
        print('这是teardownclass方法')
    
    
    def setUp(self):
        print('****这是setup方法****')
    # 自定义用例方法名必须以test***开头
    # 按照ascii码表中的字符顺序为优先级别来执行
    # teardown方法会自动在每一个测试用例后执行
    def tearDown(self):
        print('*******这是teardown方法********')
    def testabc(self):
        print('这是abc')
if __name__ == "__main__":
    # Test01().test1()
    unittest.main()