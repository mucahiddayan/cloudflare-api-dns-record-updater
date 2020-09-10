from cloudflare import CloudFlare
from config import Config

config = Config()
cloudFlare = CloudFlare(email=config['email'], apikey=config['apiKey'],zone=config['zone'])

print(cloudFlare.listRecords())