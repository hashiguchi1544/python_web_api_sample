from pprint import pprint
import requests

url = 'https://zipcloud.ibsnet.co.jp/api/search?zipcode=8480047'

response = requests.get(url)
print(response)
print(response.content)
print(response.content.decode('utf-8'))
print(response.json())

pprint(response.json())
# {'message': None,
#  'results': [{'address1': '佐賀県',
#               'address2': '伊万里市',
#               'address3': '伊万里町甲',
#               'kana1': 'ｻｶﾞｹﾝ',
#               'kana2': 'ｲﾏﾘｼ',
#               'kana3': 'ｲﾏﾘﾁｮｳｺｳ',
#               'prefcode': '41',
#               'zipcode': '8480047'}],
#  'status': 200}



print(response.json())

print(response.json()['message'])   # None
print(response.json()['results'])
print(response.json()['results'][0]['address1'])   # 佐賀県
print(response.json()['results'][0]['address2'])   # 伊万里市


