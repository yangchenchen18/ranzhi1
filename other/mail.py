from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from base.util import SendMail
import smtplib

# 邮件服务器地址
server='smtp.163.com'
# 邮件服务器端口号
prot=25
# 发件人地址-登录账号
sender='ly112425@163.com'
# 邮箱密码
pwd='BPWMWFGUAPKEUHCB'
# 收件人
receivers='ly112425@163.com;'

# 创建邮件对象
mail=MIMEMultipart()
# 填写发件人
mail['from']=sender
# 填写发件人
mail['to']=receivers
# 主题
mail['subject']='ranzhi自动化测试报告'
# 读取报告的内容
path='./selenium/ranzhi/report/report_2020-11-17 19-20-37.html'
with open(path,'rb') as file:
    report=file.read()
# 邮件正文
body=MIMEText(report,'html','utf-8')
# 将报告作为正文添加到邮件中
mail.attach(body)
# 邮件附件
attch=MIMEText(report,'base64','utf-8')
# 指定附件的类型
attch['Content-Type']='application/octet-stream'
# 指定附件的处理方式
attch['Content-Disposition']='attachment;filename=%s'%path.split('/')[-1]
# 添加附件
mail.attach(attch)
# 发送邮件
smtp=smtplib.SMTP()
# 连接服务器
smtp.connect(server,prot)
# 登录
smtp.login(sender,pwd)
# 发送
smtp.sendmail(sender,receivers.split(';'),mail.as_string())
smtp.close()
print('邮件发送完毕')