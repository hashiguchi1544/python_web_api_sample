from pprint import pprint
import requests
import os

ACCESS_KEY = os.environ['ACCESS_KEY']


def check_error(response):
    try:
        return response.json()['rest']
    except KeyError:
        return 'error'


def get_input_word():
    while True:
        user_input = input('検索ワード ：')
        url = f'https://api.gnavi.co.jp/RestSearchAPI/v3/?keyid={ACCESS_KEY}&freeword={user_input}'
        response = requests.get(url)
        checked_error = check_error(response)

        if checked_error == 'error':
            print('無効な値です。再度入力していください m(__)m')
            continue
        else:
            return checked_error


def get_rest_name_link_lists(rest_list):
    pprint(rest_list)
    for rest_info in rest_list:
        print(f"{rest_info['name']}  {rest_info['url']}")


def main():
    response = get_input_word()
    get_rest_name_link_lists(response)


if __name__ == '__main__':
    main()
