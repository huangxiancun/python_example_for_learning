# -*- coding: utf-8 -*-

# Author : 'hxc'

# Time: 2019/10/15 11:06 AM

# File_name: 'logging.py'

"""
Describe: this is a demo!
"""


import os
import logging
import time
import datetime
import re
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler

def main():
    #日志打印格式
    log_fmt = '%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s'
    formatter = logging.Formatter(log_fmt)

    #日志存放路径
    log_path = 'log/'
    #日志名称
    date = str(datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
    log_file_name =date +'.log'
    if not os.path.exists(log_path):
        os.mkdir(log_path)

    #创建TimedRotatingFileHandler对象
    log_file_handler = TimedRotatingFileHandler(filename=log_path+log_file_name, when="D", interval=1, backupCount=7)
    #log_file_handler.suffix = "%Y-%m-%d_%H-%M.log"
    #log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
    log_file_handler.setFormatter(formatter)
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger()
    log.addHandler(log_file_handler)
    #循环打印日志

    count = 0
    while count < 100:
        log.error(str(count))
        time.sleep(2)
        count = count + 1
    log.removeHandler(log_file_handler)


if __name__ == "__main__":
    main()