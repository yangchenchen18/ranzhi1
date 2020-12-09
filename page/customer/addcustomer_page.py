import os,sys
sys.path.append(os.getcwd())
from base.util import BoxDriver,BasePage
from page.login_page import LoginPage
import random

class Add_customer(LoginPage):

    def add_customer(self):
        driver=self.driver
        # 点击客户管理
        driver.click('i s-menu-1')
        
        driver.wait(2)
        # 添加区块
        driver.switch_to_frame('i iframe-1')
        driver.wait(2)
        driver.click('p 添加区块')
        driver.wait(2)
        # 选择项目
        driver.select_by_index('i blocks',random.randint(1,3))
        # 公共部分放在判断之前，标题、外观
        driver.input('i title',"12月3日")
        driver.select_by_index('id grid',random.randint(1,5))
        driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/button')
        driver.click('x //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/div/li[%d]'% random.randint(1,6))
        driver.input('i params[num]',random.randint(1,100))

        # 类型
        driver.click('id paramstype_chosen')
        driver.click('x //*[@id="paramstype_chosen"]/div/ul/li[%d]'%(random.randint(1,8)))
        # 排序
        driver.click('i paramsorderBy_chosen')
        driver.click('x //*[@id="paramsorderBy_chosen"]/div/ul/li[%d]'%(random.randint(0,3)))

        if driver.locate_elements('x //*[@id="blocks"]/option')[2].is_selected():
            driver.click('id paramstype_chosen')
            driver.click('id //*[@id="paramstype_chosen"]/div/ul/li[%d]'%(random.randint(0,6)))
        # 排序
            driver.click('i paramsorderBy_chosen')
            driver.click('id //*[@id="paramsorderBy_chosen"]/div/ul/li[%d]'%(random.randint(0,3)))
        elif driver.locate_elements('x //*[@id="blocks"]/option')[3].is_selected():
            driver.click('id paramstype_chosen')
            driver.click('id //*[@id="paramstype_chosen"]/div/ul/li[%d]'%(random.randint(0,1)))
        # 排序
            driver.click('i paramsorderBy_chosen')
            driver.click('id //*[@id="paramsorderBy_chosen"]/div/ul/li[%d]'%(random.randint(0,1)))

        driver.click("id submit")

if __name__ == "__main__":
    driver=BoxDriver()
    Add_customer=Add_customer(driver)
    Add_customer.login()
    Add_customer.add_customer()



