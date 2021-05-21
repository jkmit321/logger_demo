
import logging


PATH = 'E:\\Python_Work\\logger_demo\\'
logger = logging.basicConfig(filename=PATH+'file.log',filemode='a',
        format='%(asctime)s - %(message)s %(levelname)s %(lineno)d %(module)s %(funcName)s',level=logging.DEBUG)


def fileLog():
    for i in range(5):
        logging.debug('This is Debug message')
        logging.info('This is Info message')
        logging.warning('This is Warning message')
        logging.error('This is Error message')
        logging.critical('This is critical message')

if __name__ == '__main__':
    fileLog()


