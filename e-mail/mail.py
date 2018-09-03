#Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from src.common import config_reader
from email.header import Header
from report import test_report
'''
构造一个邮件对象就是一个Message对象。如果构造一个MIMEText对象，就表示一个文本邮件对象，如果构造一个
MIMEImage对象，就表示一个作为附件的图片，要把多个对象组合起来，就用MIMEMultipart对象，而MIMEBase可
以表示任何对象。它们的继承关系如下：
Message
+- MIMEBase
   +- MIMEMultipart
   +- MIMENonMultipart
      +- MIMEMessage
      +- MIMEText
      +- MIMEImage
'''
class Email(object):
    def __init__(self):
        '''
        初始化Email
        :param title: 邮件标题，必填。
        :param message: 邮件正文，非必填。
        :param path: 附件路径，可传入list（多附件）或str（单个附件），非必填。
        :param server: smtp服务器，必填。
        :param sender: 发件人，必填。
        :param password: 发件人密码，必填。
        :param receiver: 收件人，多收件人用“；”隔开，必填。
        '''
        '''
        构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，
        最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性
        '''
        self.email_list = config_reader.read_config().read_email_parsar()
        self.title = self.email_list[0]
        self.message = self.email_list[1]
        self.server = self.email_list[2]
        self.sender = self.email_list[3]
        self.password = self.email_list[4]
        self.receiver = self.email_list[5]

        # 构造邮件容器
        self.msg = MIMEMultipart()

    def body(self):
        ''' 邮件正文内容'''
        text = MIMEText(self.message, 'plain', 'utf-8')
        '''邮件主题、收件人、发件人（注意：前面为总容器，非文本容器！！！）'''
        self.msg['Subject'] = Header(self.title,'utf-8').encode()
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver
        self.msg.attach(text)

    # 添加图片
    def attach_image(self, msg):
        pass

    # 添加附件
    def attach_file(self):
        self.body()
        # 解决邮件中附件路径显示问题
        HtmlFile = test_report.run_report()
        HtmlFile_path = HtmlFile[0]
        HtmlFile_name = HtmlFile[1]
        # 打开附件地址
        file = MIMEApplication(open(HtmlFile_path, 'rb').read())
        file['Content-Type'] = 'application/octet-stream'
        file['Content-Disposition'] = 'attachment;filename="%s" '%HtmlFile_name
        self.msg.attach(file)

    # 执行发送命令
    def send_mail(self):
        try:
            server = smtplib.SMTP(self.server,25)
            server.set_debuglevel(1)    # 打印调试信息
            server.login(self.sender,self.password)
            print('登陆成功')

            self.attach_file()
            server.sendmail(self.sender,self.receiver,self.msg.as_string())
            print('发送成功')

        except smtplib.SMTPException as e:
            print("发送失败")

        server.quit()


Email().send_mail()