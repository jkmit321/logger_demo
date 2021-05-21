import logging
from logging.handlers import TimedRotatingFileHandler
import pymysql
from logger_demo.config import app,db
import time

FILE_PATH = 'E:\\Python_Work\\logger_demo\\log_files\\'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

consolehandler = logging.StreamHandler()
#filehandler = logging.FileHandler(filename=FILE_PATH+'db_file.log',mode='a')

consolehandler.setLevel(logging.DEBUG)
#filehandler.setLevel(logging.DEBUG)

ftr = logging.Formatter(fmt='%(asctime)s - %(message)s %(levelname)s %(lineno)d %(module)s',
                             datefmt='%a, %d %b %Y %H:%M:%S')

consolehandler.setFormatter(ftr)

logger.addHandler(consolehandler)

num = 1
class DBlogger(logging.Handler):
    def __init__(self,db_tbl_log='DB_APP_LOG'):
        logging.Handler.__init__(self)
        self.sql_conn = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='ormdb')
        self.db_tbl_log = db_tbl_log

    def emit(self,record):
        global num
        final_query = f'''insert into DB_APP_LOG values({num},{record.lineno},'{record.levelname}','{record.message}',
        '{str(record.created)}')'''
        print(final_query)
        curser = self.sql_conn.cursor()
        curser.execute(final_query)
        self.sql_conn.commit()
        num = num + 1

dbhandler = DBlogger()
dbhandler.setLevel(logging.DEBUG)
dbhandler.setFormatter(ftr)
logger.addHandler(dbhandler)

if __name__ == '__main__':

    while True:
        logger.debug('This is Debug message')
        logger.info('This is an info message')
        logger.warning('This is a warning message')
        logger.error('This is an error message')
        logger.critical('This is a critical message')
        time.sleep(5)

