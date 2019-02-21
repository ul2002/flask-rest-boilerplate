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
        self.baseUrl=config.LOGGER_HOST+':'+config.LOGGER_PORT
        self.name= config.LOGGER_USER
        self.password= config.LOGGER_PASSWORD
        self.appv= config.APP_VERSION
        self.appname= config.APP_NAME
        self.token = self.init_acra()
        self.logger = logging.getLogger('simple_example')
        log_filename = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
        fl = logging.FileHandler(filename=os.path.join(LOG_DIR, log_filename))
        self.logger.addHandler(fl)
        

    def init_acra(self):
        url = self.baseUrl+'/_session'
        data = {
            'name': self.name,
            'password': self.password 
        }
        r = requests.post(url, data = data)
        cookie = r.headers['set-cookie'].split(';')
        return cookie[0]

    def log_acra(self,level,message,cookie):
        url = self.baseUrl+'/acra-storage/_design/acra-storage/_update/report'
        headers = {
            'user-agent': 'request',
            'Cookie': cookie
        }
        data = {
            'APP_VERSION': self.appv ,
            'APP_NAME': self.appname ,
            'LEVEL': level ,
            'REPORT_ID': str(uuid.uuid4()) ,
            'STACK_TRACE': message ,
        }
        r = requests.post(url, json = data ,headers=headers)

    def info(self, message, onlylocal = 0):
        if not(onlylocal) :
            self.log_acra('info', message, self.token)
        self.logger.info(message)
        
    def error(self, message, onlylocal = 0):
        if not(onlylocal) :
            self.log_acra('error', message, self.token)
        self.logger.error(message)
        
        



