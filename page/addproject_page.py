import sys,os
sys.path.append(os.getcwd())
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
import random
from base.util import BoxDriver,BasePage
from page.login_page import LoginPage
class AddProject(LoginPage):
    def add_pro(self):

        # 点击项目，切换到iframe
        driver=self.driver
        driver.click('x //*[@id="s-menu-3"]/button/img')
        driver.switch_to_frame('id iframe-3')

    def add_project(self,title,num,uname='admin',upwd=('123456')):
        # driver = BoxDriver()
        # # driver = webdriver.Chrome()
        # driver.maximize_window()
        # driver.implicitly_wait(10)
        # driver.get('http://localhost/ranzhi/www/sys/user-login.html')

        # # 登录
        # driver.input('id account',uname)
        # driver.input('id password',upwd)
        # driver.click('id submit')
        driver=self.driver
        # 点击项目
        

        # 切换到frame中
        # frame = driver.find_element_by_id('iframe-3')
        # driver.switch_to_frame('id iframe-3')

        # for i in range(0,5):
            # 添加区块
        # driver.click('x //*[@id="dashboard"]/div[2]/a')
        # 任务列表
        driver.click('x //*[@id="blocks"]')
        driver.click('x //*[@id="blocks"]/option[2]')

        # 区块名称
        driver.input('x //*[@id="title"]',title)

        # 外观
        # 宽度
        driver.select_by_index('id grid',random.randint(1,5))

        # 颜色
        driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/button')
        random2 = random.randint(1,6)
        driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/div/li[%d]/button'%random2)

        # 类型
        driver.click('x //*[@id="paramstype_chosen"]')
        random3 = random.randint(1,4)
        driver.click('x //*[@id="paramstype_chosen"]/div/ul/li[%d]'%random3)

        # 数量
        driver.locate_element('x //*[@id="params[num]"]').clear()
        # 
        driver.input('x //*[@id="params[num]"]',num)

        # 排序
        random4 = random.randint(1,6)
        driver.click('x //*[@id="paramsorderBy_chosen"]/a/span')
        driver.click('x //*[@id="paramsorderBy_chosen"]/div/ul/li[%d]'%random4)

        # 任务状态
        driver.click('x //*[@id="paramsstatus_chosen"]/ul')
        driver.click('x //*[@id="paramsstatus_chosen"]/div/ul/li[%d]'%random.randint(1,5))

        # 保存
        driver.click('i submit')
        sleep(2)
    def add_qk(self):
        # 添加区块
        driver=self.driver
        driver.click('x //*[@id="dashboard"]/div[2]/a')
    # 断言
    def get_pname(self):
        driver=self.driver
        accounts=driver.locate_elements('x /html/body/div/div/div[1]/div/div[1]/div[1]')
        account=accounts[-1].text[3:]               
        return account
        
        
if __name__ == "__main__":
    LoginPage=AddProject(BoxDriver())
    LoginPage.login()
    LoginPage.add_pro()
    LoginPage.add_qk()
    LoginPage.add_project('11月21日',22)

