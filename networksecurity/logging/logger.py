import logging
import os
from datetime import datetime

LOG_FORMAT = f"{datetime.now().strftime('%m_%d_%Y_%H-%M-%S')}.log"

LOGS_FOLDER = 'logs'
os.makedirs(LOGS_FOLDER, exist_ok=True)

LOGS_PATH = os.path.join(os.getcwd(), LOGS_FOLDER, LOG_FORMAT)

logging.basicConfig(
    filename=LOGS_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def get_logger(name) -> logging.Logger:
    '''
    This function will return us the logger object
    '''

    try:
        logger = logging.getLogger(name)
        return logger

    except Exception as e:
        print(e)

if __name__ == '__main__':
    logger = get_logger('testing')
    logger.info('Programs Runs successfully')