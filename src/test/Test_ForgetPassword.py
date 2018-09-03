__author__ = 'Wendy_Yang'

from selenium import webdriver
import os
import unittest
from  src.common import config_reader
from log.log import Logger
from src.common import excel_reader
from report import test_report

class Test_ForgetPassword(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = config_reader.read_config().read_web_parsar()   # 调用read_config()函数并接收返回的参数url
        self.driver.get(self.url)
        self.driver.implicitly_wait(30)
        self.number = excel_reader.read_excel()
        #self.number = '13986037701'

    def tearDown(self):
        self.driver.quit()

    def test_inputPhone(self):
        phone_input = self.driver.find_element_by_id('J-m-user')

        logger = Logger().get_logger()
        for x in self.number:
            phone_input.clear()
            print('正在输入手机号',x)
            phone_input.send_keys(str(self.number))
            text = self.driver.find_element_by_xpath('//*[@id="J-m-user"]').text
            #print('text:',text)
            if text is '请输入手机号':
                logger.warning('输入手机号失败')
            else:
                logger.info('输入手机号成功')
                print('点击按钮')

    '''
    def test_inputImage(self):
        pass

    def test_inputMessage(self):
        pass
    def test_clickButton(self):
        pass
    '''



if __name__ == '__main__':
    unittest.main()
    # 开始执行测试套件



