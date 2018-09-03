import configparser
from config import config_path

class read_config(object):

    def __init__(self):
        # 方法实例化
        self.cf =  configparser.ConfigParser()

        # 读取文件（注意编码格式！）
        self.cf.read(config_path.config_path,encoding='utf-8')

        # 获取sections，返回list
        self.sections = self.cf.sections()

    def read_web_parsar(self):
        # 获取对应的section的option
        item1 = self.cf.items('web','url')
        #print(item1)
        url = item1[0][1]
        #print(url)
        return url

    def read_email_parsar(self):
        options =self.cf.options('email')
        item2 = self.cf.items('email')
        #print(item2)
        email_list = []

        i = 0
        for x in item2:
            email_list.append(item2[i][1])
            i = i + 1
        #print(email_list)
        return email_list

#read_config().read_web_parsar()
#read_config().read_email_parsar()