import sys,os
sys.path.append(os.getcwd())
from base.util import BoxDriver,BasePage,Getyaml
import yaml
class LoginPage(BasePage):
    config=Getyaml().getyml(r'E:\workspace\selenium\ranzhi\config\config.yaml')
    def login(self,uname='admin',upwd='123456'):
        '''登录操作流程'''
        driver=self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get('http://localhost/ranzhi/www/sys/user-login.html')
        # 登录
        
        ACCOUNT=self.config['LoginPage']['ACCOUNT']
        PASSWORD=self.config['LoginPage']['PASSWORD']
        SUBMIT=self.config['LoginPage']['SUBMIT']
        driver.input(ACCOUNT,uname)
        driver.input(PASSWORD,upwd)
        driver.click(SUBMIT)
        driver.wait(2)
    def logout(self):
        self.driver.click('p 签退')    
    def confim(self):
        self.driver.click('x /html/body/div[2]/div/div/div[2]/button')


    def get_real_name(self):
        acconut=self.driver.locate_element('x //*[@id="mainNavbar"]/div/ul[1]/li/a').text
        return acconut

    def get_confim(self):
        account1=self.driver.locate_element('x /html/body/div[2]/div/div/div[2]/button').text
        return account1
if __name__ == "__main__":
    
    # with open(r'E:\workspace\selenium\ranzhi\config.yaml','r',encoding='utf-8') as file:
    #     config=yaml.load(file.read(),Loader=yaml.SafeLoader)
    #     print(config)
    LoginPage(BoxDriver()).login()