import yaml
import requests

url = 'http://upload.itcollege.ee/~aleksei/eksam.yaml'


def parse_yaml(url):

    for user in yaml.load(requests.get(url).text, yaml.FullLoader):
        for k, v in user.items():

            if v["permission"] == "admin":
                return v["name"]


