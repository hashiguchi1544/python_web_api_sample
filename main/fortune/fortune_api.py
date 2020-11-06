# Web ad Fortune 無料版API http://jugemkey.jp/api/waf/api_free.php
# 原宿占い館 塔里木 http://www.tarim.co.jp/

import requests
from datetime import datetime
from main.fortune.choose_sign import choose_your_sigh


def get_today_date():
    now = datetime.now()
    ymd = now.strftime('%Y/%m/%d')
    return ymd


def check_error(response):
    try:
        return response
    except KeyError:
        return 'error'


def fetch_today_fortune(ymd) -> list:
    url = f'http://api.jugemkey.jp/api/horoscope/free/{ymd}'
    response = requests.get(url)
    response_json = response.json()['horoscope'][ymd]
    response_json = check_error(response_json)

    if response_json == 'error':
        print('占い結果が何かしらのエラーにより取得できませんでした m(__)m')
    else:
        return response_json


def fetch_your_fortune(today_fortune_list, chose_sign) -> dict:
    your_sigh_dict = today_fortune_list[chose_sign - 1]
    return your_sigh_dict


def show_your_sign(your_sign_dict):
    print(f"今日の{your_sign_dict['sign']}の運勢は、第{your_sign_dict['rank']}位です。")
    print(f"ラッキーアイテムは、{your_sign_dict['item']}です。")
    print(f"ラッキーカラーは、{your_sign_dict['color']}です。")
    print(f"金運は、{your_sign_dict['money']}/5 です。")
    print(f"仕事運は、{your_sign_dict['job']}/5 です。")
    print(f"恋愛運は、{your_sign_dict['love']}/5 です。")
    print(f"{your_sign_dict['content']}")


def main():
    year_month_day = get_today_date()
    today_fortune_list = fetch_today_fortune(year_month_day)
    chose_sign = choose_your_sigh()
    your_sign_dict = fetch_your_fortune(today_fortune_list, chose_sign)
    show_your_sign(your_sign_dict)


if __name__ == '__main__':
    main()
