import sys,os
sys.path.append(os.getcwd())
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
from base.util import BoxDriver,BasePage
from page.login_page import LoginPage
import random

class AddOffice(LoginPage):

    def switch_frame(self):
        self.driver.click('x //*[@id="s-menu-2"]/button/img')
        self.driver.switch_to_frame('id iframe-2')
    def add_office(self,title,num,uname='admin',upwd='123456'):
    #     driver=BoxDriver()
    #     driver.maximize_window()
    #     driver.implicitly_wait()
    #     driver.get('http://localhost/ranzhi/www/sys/user-login.html')
    # #    登录
    #     driver.input('id account',uname)
    #     driver.input('id password',upwd)
    #     driver.click('id submit')
        driver=self.driver
        sleep(2)
        # 点击日常办公
        # driver.click('x //*[@id="s-menu-2"]/button/img')
    # 进入frame
        # driver.switch_to_frame('id iframe-2')
    # 定位添加区块
        # for i in range(1,5):
            # title='事情%d'%i
        # driver.click('p 添加区块')
        # 选择日历或者办公
        driver.click('id blocks')
        driver.select_by_index('id blocks',random.randint(1,2))
        # 标题
        driver.input('id title',title)
        driver.select_by_index('id grid',random.randint(1,5))
        driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/button')
        driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/div/li[%d]'% random.randint(1,6))
        # 保存
        driver.click('id submit')
        if driver.locate_element('x //*[@id="blocks"]/option[2]').text=='系统办公':
            driver.locate_element('id params[num]').clear()
            driver.input('id params[num]',num)
        sleep(2)
    # driver.close()
    def add_off(self):
        self.driver.click('p 添加区块')
    # 断言
    def get_pname(self):
        accouts=self.driver.locate_elements('x /html/body/div/div/div[1]/div/div[1]/div[1]')
        accout=accouts[-1].text[3:]
        return accout
if __name__ == "__main__":
    driver = BoxDriver()
    office= AddOffice(driver)
    office.login()
    office.switch_frame()
    office.add_off()
    office.add_office("11月22日",'30')
