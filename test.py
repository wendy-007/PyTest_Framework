import smtplib
from email.mime.text import MIMEText

msg_from = 'wendy930915@sina.com'
passwd = '15926470053'
msg_to = '675760607@qq.com'

subject = "python邮件测试"
content = "这是我使用python smtplib及email模块发送的邮件"

msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
try:
    # s = smtplib.SMTP_SSL("smtp.163.com",465)
    s = smtplib.SMTP("smtp.sina.com", 25)
    s.login(msg_from, passwd)
    s.set_debuglevel(1)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print("发送成功")
except smtplib.SMTPException as e:
    print("发送失败")
finally:
    s.quit()