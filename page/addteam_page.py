import sys,os
sys.path.append(os.getcwd())
from base.util import BoxDriver
from page.login_page import LoginPage
import random
class AddTeam(LoginPage):
    # 先继承loginpage页面进行登录
    def addteam(self,title,num,uname='admin',upwd='123456'):
        driver=self.driver
        # 点击团队
        driver.click('x //*[@id="s-menu-6"]/button/img')
        # 强制等待页面刷新
        driver.wait(2)
        # 添加区块
        driver.switch_to_frame('id iframe-6')
        driver.click('p 添加区块')
        driver.wait(2)
        # 随机选择一个项目
        driver.click('i blocks')
        driver.select_by_index('id blocks',random.randint(1,2))
        # 添加区块名称
        driver.input('id title',title)
        # 随机点击宽度
        driver.click('i grid')
        driver.select_by_index('id grid',random.randint(0,5))
        # 随机选择颜色
        # driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/button')
        # driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/div/li[%d]/button'%(random.randint(1,6)))
        driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/button')
        random2 = random.randint(1,6)
        driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/div/li[%d]/button'%random2)
        
        # 填写数量
        driver.input('id params[num]',num)
        # # 如果选择帖子，则需要增加一个类型
        if driver.locate_element('x //*[@id="blocks"]/option[3]').text=='帖子列表':
            driver.click('x //*[@id="paramstype_chosen"]')
            driver.click('x //*[@id="paramstype_chosen"]/div/ul/li[%d]'%(random.randint(1,2)))
        
        driver.click('id submit')
        driver.wait(2)
        driver.close()

if __name__ == "__main__":
    driver=BoxDriver()
    AddTeam=AddTeam(driver)
    AddTeam.login()
    AddTeam.addteam('自动化测试','15')