import sys,os
sys.path.append(os.getcwd())
from base.util import BoxDriver
from page.login_page import LoginPage
import random
class AddMoney(LoginPage):

    def switch_frame(self):
        driver=self.driver
        driver.click("x //*[@id='s-menu-5']/button")
    #     accout1=len(driver.locate_elements("x //*[@id='dashboard']/div/div"))
    #     return accout1
    # def s_frame(self):
        self.driver.wait(2)
        # 切换表单
        self.driver.switch_to_frame("i iframe-5")
        
    def add_qk(self):
        self.driver.wait(2)
        self.driver.click("p 添加区块")
    def add_money(self,title,num,uname='admin',upwd='123456'):
        driver=self.driver
        driver.wait(2)
        # 添加区块
        # 选择区块
        # driver.click('i blocks')
        driver.select_by_index('i blocks',random.randint(1,5))
        driver.input('i title',title)
        # driver.click('x //*[@id="blocks"]/option[%d]'%(random.randint(1,6)))
        driver.select_by_index('i grid',random.randint(0,5))
        # 选择颜色
        driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/button')
        driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/div/li[%d]/button'%(random.randint(1,6)))
        
        # if driver.locate_element('x //*[@id="blocks"]/option[2][@value="depositor"]').is_selected():

        # 添加标题
            # driver.input('i title',"11月26日")
         # 选择宽度
        
        if driver.locate_element('x //*[@id="blocks"]/option[3][@value="trade"]').is_selected():
            
            # 添加标题
            
            #  # 选择宽度
            # driver.click('i grid')
            # driver.select_by_index('i grid',random.randint(0,5))
            # # 选择颜色
            # driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/button')
            # driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/div/li[%d]/button'%(random.randint(1,6)))
            # 数量
            driver.input('i params[num]',num)
            # 排序
            driver.click('x //*[@id="paramsorderBy_chosen"]/a/span')
            driver.click('x //*[@id="paramsorderBy_chosen"]/div/ul/li[%d]'%(random.randint(1,2)))
            # 交易
            driver.click('i paramstype_chosen')
            driver.click('x //*[@id="paramstype_chosen"]/div/ul/li[%d]'%(random.randint(1,3)))
            
        elif driver.locate_element('x //*[@id="blocks"]/option[4][@value="baseFacts"]').is_selected():
            # driver.input("i title",'11月26日收支概况')
            
            # 数量
            driver.input('i params[num]',num)
            # 排序
            driver.click('x //*[@id="paramsorderBy_chosen"]/a/span')
            driver.click('x //*[@id="paramsorderBy_chosen"]/div/ul/li[%d]'%(random.randint(1,2)))
           
        elif driver.locate_element('x //*[@id="blocks"]/option[5][@value="provider"]').is_selected():
            # driver.input("i title",'11月26日供应商')
            
            # 数量
            driver.input('i params[num]',num)
            # 排序
            driver.click('x //*[@id="paramsorderBy_chosen"]/a/span')
            driver.click('x //*[@id="paramsorderBy_chosen"]/div/ul/li[%d]'%(random.randint(1,2)))

            
        elif driver.locate_element('x //*[@id="blocks"]/option[6][@value="report"]').is_selected():
            # driver.input("i title",'11月26日报表')
            # 报表
            driver.click('x //*[@id="paramstype_chosen"]')
            driver.click('x //*[@id="paramstype_chosen"]/div/ul/li[%d]'%(random.randint(1,2)))
                #报表
            driver.click('x //*[@id="paramsgroupBy_chosen"]')
            driver.click('x //*[@id="paramsgroupBy_chosen"]/div/ul/li[%d]'%(random.randint(1,2)))
                #货币
            driver.click('x //*[@id="paramscurrency_chosen"]') 
            driver.click('x //*[@id="paramscurrency_chosen"]/div/ul/li[%d]'%(random.randint(1,2)))

        driver.click('i submit')
    
    # 断言
        # accouts=driver.locate_elements("x /html/body/div/div/div[1]/div/div[1]/div[1]")
        # accout=accouts[-1]
        # print(accout.text)
        # assert accout.text==title
    def get_mname(self):
        accouts=self.driver.locate_elements("x //*[@id='dashboard']/div/div")
        accout=len(accouts)
        return accout


if __name__ == "__main__":
    driver=BoxDriver()
    addmoney=AddMoney(driver)
    addmoney.login()
    addmoney.switch_frame()
    addmoney.add_qk()
    addmoney.add_money("12月2日","2")
    