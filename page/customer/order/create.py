import os,sys
sys.path.append(os.getcwd())
import random
from base.util import BasePage,BoxDriver
from page.login_page import LoginPage
from page.customer.order.addorder import AddOrder

class Operation(LoginPage):

    def operation(self):
        driver=self.driver
        # 点击客户管理

        driver.click('id s-menu-1')
        driver.wait(2)
        driver.switch_to_frame('i iframe-1')
        # 点击订单
        driver.click('p 订单')
        # 查看
        driver.click('p 查看')



if __name__ == "__main__":
    driver=BoxDriver()
    open=Operation(driver)
    open.login()
    open.operation()