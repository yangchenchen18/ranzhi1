# 工作簿workbook
# 工作表 worksheet
# 单元格 cell
import openpyxl
import csv
# workbook = openpyxl.load_workbook(r'selenium\ranzhi\data.xlsx')
# # 获取指定的工作表
# login_success=workbook['login_success']
# list=[]
# for r in login_success:
#     t=[]
#     for cell in r:
#         # print(cell.value)
#         t.append(cell.value)
#     print(t)
#     list.append(tuple(t))
# # l=[r for r in login_success]

with open(r'E:\workspace\selenium\ranzhi\data.csv','r',encoding='utf-8') as file:
    content=file.readlines()
    print(content)
    list2=[]
    for i in content:
        print(i)
     
        a=i.strip().split(',')
        print(tuple(a))
        list2.append(tuple(a))
        print(list2)

    # list = [tuple(i.strip().split(',')) for i in content]
    # print(list)
        
        
        
        
        

      
