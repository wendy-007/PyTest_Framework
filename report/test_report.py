import time
from report import report_path
import unittest
from src.test import test_path
import HTMLTestRunner

def run_report():
    # 获取系统当前时间（通用方法）
    now= time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

    # 定义测试报告的名称和存储位置
    HtmlFile_name = 'HTMLReport-' +now + ".html"
    HtmlFile_path = report_path.report_path + HtmlFile_name
    HtmlFile = [HtmlFile_path,HtmlFile_name]

    # 构造suite（discover方法），加载测试用例
    suit = unittest.TestLoader().discover(test_path.test_suit_dir,pattern='Test_*.py')

    # 以wb(可写的二进制文件)形式，打开文件，若文件不存在，则先执行创建，再执行打开
    file = open(HtmlFile_path,'wb')

    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    with open(HtmlFile_path,'wb') as file:
        # 调用HTMLTestRunner生成报告
        runner =HTMLTestRunner.HTMLTestRunner(
            # 制定测试报告的文件
            stream=file,
            # 测试报告的标题
            title = '忘记密码界面测试报告',
            # 测试报告的副标题
            description = u'用例执行情况（Win7 64位）'
        )

        # 开始执行测试套件（重点！这里是入口！后面将分离开）
        runner.run(suit)


    return HtmlFile     # 返给Email模块