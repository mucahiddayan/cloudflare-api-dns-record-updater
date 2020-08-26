from cloudflare import CloudFlare
import yaml

with open(r'./config.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    config = yaml.load(file, Loader=yaml.FullLoader)

    cloudFlare = CloudFlare(email=config['email'], apikey=config['apiKey'],zone=config['zone'])
    print(cloudFlare.updateRecordIpById("aba7977d352ada21e607cc1f3afe6209"))
    print(cloudFlare.updateRecordIpByName("xn--mcahiddayan-thb.com"))
