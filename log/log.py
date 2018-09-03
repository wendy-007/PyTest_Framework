'''封装logging库，使框架可以很简单地打印日志（输出到控制台以及日志文件）'''
import logging
from logging.handlers import TimedRotatingFileHandler
import os
from log.log_path import log_path
import time

# 当一个项目比较大的时候，不同的文件中都要用到Log,可以考虑将其封装为一个类来使用
class Logger(object):
    def __init__(self):
        # 使用 time.strftime（），使命名文件名包含当前时间
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        self.logger = logging.getLogger('password_test')
        self.logger.setLevel(logging.DEBUG)                # 注意：如果不设置，默认等级是WARNING
        self.logfile_name = 'ForgetPassword_test-'+now+'.log'   # 日志名称
        self.backup_count = 5

        # 设置日志输出级别
        self.console_output_level = 'WARNING'
        self.file_output_level = 'INFO'
        
        # 设置日志格式
        self.formate = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")


    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:       # 避免重复日志
            console_handler = logging.StreamHandler()           # 创建一个句柄
            console_handler.setFormatter(self.formate)          # 设置输出格式
            console_handler.setLevel(self.console_output_level) # 设置输出级别
            self.logger.addHandler(console_handler)             # 添加句柄

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(log_path, self.logfile_name),
                                                    when='D',       # Days，表示每天产生一个日志文件
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            file_handler.setFormatter(self.formate)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)

            return self.logger

if __name__ == '__main__':
    log_print = Logger().get_logger()
