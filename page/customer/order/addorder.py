import os,sys
sys.path.append(os.getcwd())
from base.util import BoxDriver,BasePage
from page.login_page import LoginPage
import random
class AddOrder(LoginPage):
    def addorder(self):
        driver=self.driver
        # 点击项目
        driver.click("i s-menu-1")
        driver.wait(2)
        driver.switch_to_frame('i iframe-1')
        # 点击订单
        driver.click('p 订单')
        driver.wait(2)
        # 创建订单
        driver.click('p 创建订单')
        # 点击新建
        driver.click('i createCustomer')
        # 输入姓名
        driver.input('i name',"12月4日")
        # 联系人
        driver.input('i contact',"闪电")
        # 电话
        driver.input('i phone',"1234567901")
        # 邮箱
        driver.input('i email',"123@qq.com")
        # qq
        driver.input('i qq',"123455")
        # 产品新建
        driver.click('i createProduct')
        driver.input('i productName',"12月4日")
        # 代号
        driver.input('i code',"123abc")
        # 产品线
        # driver.input('i line',"1号线")
        # 类型
        driver.select_by_index('i type',random.randint(0,2))
        # 金额
        driver.select_by_index('i currency',random.randint(0,1))
        driver.input('i plan',"100")
        # 保存
        driver.click('i submit')




if __name__ == "__main__":
    driver=BoxDriver()
    addorder=AddOrder(driver)
    addorder.login()
    addorder.addorder()



