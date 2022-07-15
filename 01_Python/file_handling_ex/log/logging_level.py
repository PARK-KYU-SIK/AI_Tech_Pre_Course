import logging
from operator import mod

from click import echo




import logging

if __name__ == '__main__' :
    logger = logging.getLogger('main')
    logging.basicConfig(level = logging.DEBUG)
    logger.setLevel(logging.INFO)

    # steam_handler = logging,logging.FileHandler('my.log', mode = 'a', encoding = 'utf8')
    # logger.addHandler(steam_handler)
        
    logging.debug('프로그램 틀림')
    logging.info('확인필요')
    logging.warning('조심하시오')
    logging.error('에러')
    logging.critical('망했다')