"""
* @author: Awwal Mohammed
* date: 06-11-21
* program title: main_routine.py

description:
\t This program is expected to carry out an operation such that given a number of pennies
\t will calculate the minimum number of Sterling coins equivalent to that amount.
"""
import math
import re

from terminal_graphics import MinSterlingTerminal


def get_coins(cur_val, signal):
    """
    get_coins(cur_val, signal) -> [minimum coins, coins map]

    Return an array containing a string describing the minimum coins that represents cur_val,
    and a dictionary that indexes the number of coins produced.
    The signal parameter allows pound coins and pennies to be treated uniquely.

    :param cur_val: numeric monetary value corresponding with the user input.
    :param signal: pound coin or pennies, allows for specialized arithmetic.
    :return: a list containing a string and a dictionary, both describing the minimum coins.
    """
    one_pound = 0
    two_pounds = 0
    one_pennie = 0
    two_pennies = 0
    five_pennies = 0
    ten_pennies = 0
    twenty_pennies = 0
    fifty_pennies = 0

    cur_val = round(cur_val * 100, 2) if signal is '£' else cur_val

    two_pounds = cur_val / 200
    cur_val %= 200
    one_pound = cur_val / 100
    cur_val %= 100
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
    results = [result, coins]

    return results


# display welcome message ASCII banner
terminal = MinSterlingTerminal()
terminal.show_welcome_msg()

# main loop
while True:
    # input prompt
    print("ENTER PENNIES (e.g. £2, £1, 50p, 20p, 10p, 5p, 2p and 1p): ")

    # priliminary filtering
    user_input = input().__str__().lower()
    copy_input = user_input

    is_pennies = False
    is_pounds = False
    is_pound_pence = False
    is_sing_or_doub = False
    is_pound_decimal = False
    is_missing_pence = False
    is_sing_dig_pound = False

    is_pennies = True if \
        user_input.endswith('p') and '.' not in user_input and \
        '£' not in user_input and user_input.count('p') <= 1 else False
    is_pound_pence = True if \
        not is_pennies and user_input.endswith('p') and \
        user_input.count('p') == 1 and user_input.count('.') == 1 else False
    is_pound_decimal = True if \
        '.' in user_input and '£' not in user_input and 'p' not in user_input else False
    try:
        if '.' in user_input or '£' in user_input:
            float(user_input.replace('£', ''))
            is_pounds = True
    except Exception:
        is_pounds = False
    try:
        int(user_input.replace('£', ''))
        is_sing_or_doub = True if not is_pennies and '£' not in user_input and not is_pounds else False
    except Exception:
        is_sing_or_doub = False
    is_missing_pence = True if '£' in user_input and 'p' in user_input and '.' not in user_input else False
    if is_missing_pence:
        is_pennies = False
        is_pounds = False
        is_pound_pence = False
        is_sing_or_doub = False
        is_pound_decimal = False

    user_input = user_input.replace('p', '') if is_pennies else user_input
    cur_pat = "(?:[\£\]{1}[,\d]+.?\d*)"  # regex pattern for finding currency or cash amount strings

    try:    # coin processing mechanism
        if is_pennies:                      # e.g. 123p, 4p, 167p, etc.
            temp_input = user_input.replace('p', '')
            temp_input = round(float(temp_input), 2)
            user_input = '£' + str(temp_input)
            amount = re.search(cur_pat, user_input)[0].replace('£', '')
            print(str(copy_input), ' = ', get_coins(temp_input, signal='p')[0])
            terminal.show_result_table(     # describe coins in a terminal table
                user_input=copy_input, data=get_coins(temp_input, signal='p')[1])

        elif is_pounds or is_pound_pence:   # e.g. £1.33, 6.235p, 001.61p
            if '£' in user_input:
                temp_input = user_input.replace('£', '').replace('p', '')
                temp_input = round(float(temp_input), 2)
                user_input = '£' + str(temp_input)
                amount = re.search(cur_pat, user_input)[0]
                print(str(copy_input), ' = ', get_coins(temp_input, signal='£')[0])
                terminal.show_result_table(
                    user_input=copy_input, data=get_coins(temp_input, signal='£')[1])
            else:                           # e.g. 1.97, 10.75, 0.56, etc.
                temp_input = round(float(user_input.replace('p', '')), 2)
                print(str(copy_input), ' = ', get_coins(temp_input, signal='£')[0])
                terminal.show_result_table(
                    user_input=copy_input, data=get_coins(temp_input, signal='£')[1])

        elif is_sing_or_doub:  # ...or more. # e.g. 6, 75, etc.
            print(str(copy_input), ' = ', get_coins(int(user_input), signal='p')[0])
            terminal.show_result_table(
                user_input=copy_input, data=get_coins(int(user_input), signal='p')[1])

        elif is_pound_decimal:              # e.g. £1.97p, £1.256532677p, etc.
            print(str(copy_input), ' = ', get_coins(round(float(user_input), 2), signal='£')[0])
            terminal.show_result_table(
                user_input=copy_input, data=get_coins(round(float(user_input), 2), signal='£')[1])

        elif is_missing_pence:              # e.g. £1.p, £.75p, etc.
            temp_input = round(float(user_input.replace('p', '').replace('£', '')), 2)
            print(str(copy_input), ' = ', get_coins(temp_input, signal='£')[0])
            terminal.show_result_table(user_input=copy_input, data=get_coins(temp_input, signal='£')[1])
        else:   # invalid input -> just print 0
            print(0)
        print()
    except Exception:
        pass
