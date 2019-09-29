import smtplib
from email.mime.text import MIMEText
from email.header import Header
from common.commonVar import CommonVar
'''
    发送邮件
    @auther zw
    2019-4-30
'''
class SendEmail():
    #自动发送邮件
    def send_email(new_report):
        #读取测试报告中的内容作为邮件的内容
        with open(new_report,'r',encoding='utf8') as f:
            mail_body = f.read()
        #发件人地址
        from_addr = CommonVar.FROM_ADDR
        #收件人地址
        to_addr = CommonVar.TO_ADDR
        #发送邮箱的服务器地址
        mail_server = CommonVar.MAIL_SERVER
        #邮件的标题
        subject = CommonVar.SUBJECT
        #发件人的邮箱地址
        username = CommonVar.EM_USERNAME
        password = CommonVar.EM_PASSWORD
        #邮箱的内容和标题
        message = MIMEText(mail_body,'html','utf8')
        message['Subject'] = Header(subject,charset='utf8')
        #发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(mail_server)
        smtp.login(username,password)
        smtp.sendmail(from_addr,to_addr.split(','),message.as_string())
        smtp.quit()
