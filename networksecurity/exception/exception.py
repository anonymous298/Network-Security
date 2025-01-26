from linecache import getline
import sys
from networksecurity.logging.logger import get_logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()

        self.linno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
    
    def __str__(self):
        return f'Error occured in python sript [{self.file_name}] lineno [{self.linno}] error message [{str(self.error_message)}]'

    
if __name__ == '__main__':
    logger = get_logger('testing')

    try:
        logger.info('Converting string to integer')
        a = int('f')

    except Exception as e:
        logger.error(f'Error Occured {e}')
        raise NetworkSecurityException(e, sys)