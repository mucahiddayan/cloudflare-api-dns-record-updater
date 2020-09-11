from cloudflare import CloudFlare
from config import Config

config = Config()
cloudFlare = CloudFlare(email=config['email'], apikey=config['apiKey'],zone=config['zone'])

# print(cloudFlare.listRecords())
# print(cloudFlare.findRecordByName("xn--mcahiddayan-thb.com"))
print(cloudFlare.findRecordById("9ccdfe71e7913f4ec32bc74a70546b64"))