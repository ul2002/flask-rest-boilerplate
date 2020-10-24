import os
import uuid
import logging
import datetime
import requests
from app.main.config import Config as config
from definitions import LOG_DIR


class logger:
    
    def __init__(self):
        logging.basicConfig(
            format='%(asctime)s %(levelname)s %(message)s', 
            level=logging.INFO, 
            datefmt='%m/%d/%Y %I:%M:%S %p'
        )
       
        self.logger = logging.getLogger('simple_example')
        log_filename = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
        fl = logging.FileHandler(filename=os.path.join(LOG_DIR, log_filename))
        self.logger.addHandler(fl)
        

    def info(self, message):
        self.logger.info(message)
        
    def error(self, message):
        self.logger.error(message)

    def warning(self, message):
        self.logger.warning(message)
        
        



