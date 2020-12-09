import sys,os
sys.path.append(os.getcwd())
from selenium import webdriver
from selenium.webdriver.support.select import Select
import random
from base.util import BoxDriver,BasePage
from page.login_page import LoginPage

class AddUser(LoginPage):
    def add_u(self):
        # 点击添加用户及切换表单
        driver=self.driver
        # 添加成员
        driver.wait(3)
        driver.click('x //*[@id="s-menu-superadmin"]/button')
        # 切换到frame中
        

    def add_user(self,username,password,uname='admin',upwd='123456'):
        
        # driver = webdriver.Chrome()
        # driver = BoxDriver()
        
        # driver.maximize_window()
        # driver.implicitly_wait()

        # driver.get('http://localhost/ranzhi/www/sys/user-login.html')

        # # 登陆
        # driver.input('id account',uname)
        # driver.input('id password',upwd)
        # driver.click('id submit')
        driver=self.driver
        driver.switch_to_frame('id iframe-superadmin')
        driver.click('p 添加成员')
        # 添加成员
        # driver.wait(3)
        # driver.click('x //*[@id="s-menu-superadmin"]/button')


        # # 切换到frame中
        # driver.switch_to_frame('id iframe-superadmin')

        # # 点击"添加成员"
        # driver.click('p 添加成员')

        # for i in range(30,33):
        # username = 'user%d'%i
        
        # 添加成员
        driver.input('i account', username)
        driver.input('id realname', username)
        # 性别
        driver.click('x /html/body/div/div/div[2]/div/div[2]/form/table/tbody/tr[3]/td/label[%d]/input'%(random.randint(1,2)))
        
        # 选择部门
        driver.select_by_index('id dept',random.randint(1,6)) # 根据下标来选中

        # 选择角色
        driver.select_by_index('id role', random.randint(1,16)) # 根据下标来选中

        # 密码
        driver.input('id password1', password)
        driver.input('id password2', password)

        driver.input('id email','%s@163.com'%username)

        # 保存
        driver.click('id submit')

        driver.wait(3)
    def get_name(self):
        driver=self.driver
        # 跳转到最后一页
        driver.input('id _pageID', '10000')
        driver.click('id goto')
        driver.wait(1)

        # 断言
        accounts = driver.locate_elements('xpath /html/body/div/div/div/div[2]/div/div/table/tbody/tr/td[3]')
        account = accounts[-1]
        # assert account.text == username
        return account.text

        # 添加下一个成员
    def addnext(self):
        driver=self.driver
        driver.click('xpath /html/body/div/div/div/div[1]/div/div[2]/a[1]')

        driver.wait(2)
        # driver.close()

if __name__ == "__main__":
    driver=BoxDriver()
    adduser=AddUser(driver)
    adduser.login()
    adduser.add_u()
    adduser.add_user('lil','123456')