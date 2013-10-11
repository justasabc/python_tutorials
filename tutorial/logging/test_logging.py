#http://docs.python.org/3/howto/logging.html
import logging
print(__name__)
FORMAT = '%(asctime)-15s %(name)-8s %(levelname)s %(message)s'
logging.basicConfig(filename='example.log',level=logging.DEBUG,format=FORMAT)
# method1: logging
# name = root
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.warning('%s before you %s','look','leap')

# method2: logging.getLogger('xxx')
# name = xxx
logger = logging.getLogger('mylogger')
logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.warning('%s before you %s','look','leap')
