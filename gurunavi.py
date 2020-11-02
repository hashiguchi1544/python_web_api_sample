from pprint import pprint
import requests
import os

ACCESS_KEY = os.environ['ACCESS_KEY']
freeword = input('検索ワード :')
print('---------------------------------')
url = f'https://api.gnavi.co.jp/RestSearchAPI/v3/?keyid={ACCESS_KEY}&freeword={freeword}'

response = requests.get(url)
rest_list = response.json()['rest']
for rest in rest_list:
    print(rest['name'])