import yaml
import requests

url = 'http://upload.itcollege.ee/~aleksei/eksam.yaml'


def parse_yaml(url):

    for user in yaml.load(requests.get(url).text, yaml.FullLoader):
        print(user)
        for k, v in user.items():

            if v["permission"] == "admin":
                return k


if __name__ == '__main__':
    parse_yaml(url)
