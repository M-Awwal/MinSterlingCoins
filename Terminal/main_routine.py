"""
@author: Awwal Mohammed
date: 06-11-21
program title: main_routine.py

description:
This program is expected to carry out an operation such that given a number of pennies\
will calculate the minimum number of Sterling coins equivalent to that amount.
"""
import math
import re


def get_coin(cur_val, signal):
    one_pound = 0
    two_pounds = 0
    one_pennie = 0
    two_pennies = 0
    five_pennies = 0
    ten_pennies = 0
    twenty_pennies = 0
    fifty_pennies = 0

    two_pounds = cur_val / 200
    cur_val %= 200

    one_pound = cur_val / 100
    cur_val %= 100

    cur_val = round(cur_val*100, 2) if signal is '£' else cur_val
    fifty_pennies = cur_val / 50
    cur_val %= 50

    twenty_pennies = cur_val / 20
    cur_val %= 20

    ten_pennies = cur_val / 10
    cur_val %= 10

    five_pennies = cur_val / 5
    cur_val %= 5

    two_pennies = cur_val / 2
    cur_val %= 2

    one_pennie = math.ceil(cur_val)

    coins = {"£2": int(two_pounds), "£1": int(one_pound),
             "50p": int(fifty_pennies), "20p": int(twenty_pennies),
             "10p": int(ten_pennies), "5p": int(five_pennies),
             "2p": int(two_pennies), "1p": int(one_pennie)}

    result = str()
    for c in coins:
        if coins[c] != 0:
            result += str(coins[c]) + ' x ' + c + ', '
    result = result[:-1] if result.endswith(', ') or result.endswith(',') else result

    return result


while True:
    # input prompt
    print("ENTER PENNIES (e.g. £2, £1, 50p, 20p, 10p, 5p, 2p and 1p): ")

    # priliminary filtering
    is_pennies = False
    user_input = input().__str__().lower()
    copy_input = user_input
    is_pennies = True if user_input.endswith('p') and '.' not in user_input and '£' not in user_input and user_input.count('p') is 1 else False
    user_input = user_input.replace('p', '') if is_pennies else user_input
    cur_pat = "(?:[\£\]{1}[,\d]+.?\d*)"  # regex pattern for finding currency or cash amount strings

    # coin processing mechanism
    try:
        if is_pennies:
            # logic for processing pennies
            temp_input = user_input.replace('p', '')
            temp_input = round(float(temp_input), 2)
            user_input = '£' + str(temp_input)
            amount = re.search(cur_pat, user_input)[0].replace('£', '')
            print(str(copy_input), ' = ', get_coin(temp_input, signal='p'))
        else:
            # logic for processing pounds
            if '£' in user_input:
                temp_input = user_input.replace('£', '')
                temp_input = round(float(temp_input), 2)
                user_input = '£' + str(temp_input)
                amount = re.search(cur_pat, user_input)[0]
                print(str(copy_input), ' = ', get_coin(temp_input, signal='£'))
            print()
    except Exception as e:
        print(e)

