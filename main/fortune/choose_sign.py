def choose_your_sigh():
    while True:
        input_num = int(input('あなたの星座を以下の番号を半角で選んでください：\n'
                              '1: 牡羊座\n'
                              '2: 牡牛座\n'
                              '3: 双子座\n'
                              '4: 蟹座\n'
                              '5: 獅子座\n'
                              '6: 乙女座\n'
                              '7: 天秤座\n'
                              '8: 蠍座\n'
                              '9: 射手座\n'
                              '10: 山羊座\n'
                              '11: 水瓶座\n'
                              '12: 魚座\n'))
        if 1 <= input_num <= 12:
            return input_num
        else:
            print('無効な値です。やり直してください m(__)m')
