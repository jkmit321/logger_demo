
FILE_PATH = 'E:\\Python_Work\\logger_demo\\log_files\\'

import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

consolehand = logging.StreamHandler()
filehand = logging.FileHandler(filename=FILE_PATH+'app.log',mode='a')
timerotatehand = TimedRotatingFileHandler(filename=FILE_PATH+'application.log',when='M',backupCount=10)

formater = logging.Formatter(fmt='%(asctime)s - %(message)s %(levelname)s %(lineno)d %(module)s',
                             datefmt='%a, %d %b %Y %H:%M:%S')

consolehand.setFormatter(formater)
filehand.setFormatter(formater)
timerotatehand.setFormatter(formater)

logger.addHandler(consolehand)
logger.addHandler(filehand)
logger.addHandler(timerotatehand)

import time

if __name__ == '__main__':

    while True:
        logger.debug('This is Debug message')
        logger.info('This is Info message')
        logger.warning('This is Warning message')
        logger.error('This is Error message')
        logger.critical('This is Critical message')
        time.sleep(5)

