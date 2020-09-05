from cloudflare import CloudFlare
import yaml
import os
import datetime
import logging
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname,'config.yaml')
log_file = os.path.join(dirname,'main.log')

import logging
logger = logging.getLogger('CloudFlareDNSUpdater')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(log_file)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

with open(filename, mode="r") as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    config = yaml.load(file, Loader=yaml.FullLoader)

    cloudFlare = CloudFlare(email=config['email'], apikey=config['apiKey'],zone=config['zone'])
    currentIp = cloudFlare._getIp()
    if  currentIp != config.get('lastIp', "NOT"):
        config.update({'lastIp': currentIp})
        logger.info('Ip is changed. It will be updated ')
        logger.info(datetime.datetime.now())

        with open(filename,mode='w') as fileToWrite:
            yaml.safe_dump(config,fileToWrite,encoding='utf-8', allow_unicode=True)
            cloudFlare.updateRecordIpById("aba7977d352ada21e607cc1f3afe6209")
            cloudFlare.updateRecordIpByName("xn--mcahiddayan-thb.com")
    else:
        logger.info('Ip is not changed')






