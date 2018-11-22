import logging
from logging.handlers import RotatingFileHandler
'''
RotatingFileHandler 的回滚时刻是当日志文件的大小达到一定值。
当日志文件的大小达到指定值的时候，RotatingFileHandler 会将日
志文件重命名存档，然后打开一个新的日志文件。
'''
import os
import time
from Common import dri_config

fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
'''
format: 指定输出的格式和内容：
%(asctime)s   :日志事件发生的时间
%(levelname)s :该日志记录的文字形式的日志级别
%(filename)s  :pathname的文件名部分，包含文件后缀
%(funcName)s  :%(funcName)s
%(lineno)d    :打印日志的当前行号，line；行
%(message)s   :日志记录的文本内容
'''
datefmt = '%a, %d %b %Y %H:%M:%S'  #日期的格式

handler_1 = logging.StreamHandler()
'''
StreamHandler()：能够将日志信息输出到sys.stdout, sys.stderr 或者类文件对象
'''

curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())
'''
time.localtime:时间，本地时间
'''

handler_2 = RotatingFileHandler(dri_config.logs_dir+"/Web_Autotest_{0}.log".format(curTime),backupCount=20,encoding='utf-8')
'''
backupCount:日志备份计数
encoding：编码
'''
#设置rootlogger 的输出内容形式，输出渠道
logging.basicConfig(format=fmt,datefmt=datefmt,level=logging.INFO,handlers=[handler_1,handler_2])
'''
basicConfig：基本配置
datefmt: 指定时间格式，同time.strftime()
level: 设置日志级别，默认为logging.WARNING
stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，
默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略
'''