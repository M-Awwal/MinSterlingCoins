"""
* @author: Awwal Mohammed
* date: 09-11-21
* program title: test_skeleton.py

description:
\t This program holds the structure for methods being called by test_cases.py,
\t which in turn performs individual explicit tests based on
\t the provided test data (refer to README.md).
\t As you'll see, this source file contains segments of code identical to main_routine.py.
\t Elaborate comments are ignored, but can be referenced from the main_routine.py.

"""
import logging
import math
import re
import test_terminal_graphics


def get_coins(cur_val, signal):
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


terminal = test_terminal_graphics.MinSterlingTerminal()


def main(data):

    # priliminary filtering
    user_input = data.__str__().lower()
    copy_input = user_input

    is_pennies = is_pounds = is_pound_pence = is_sing_or_doub = \
        is_pound_decimal = is_missing_pence = is_sing_dig_pound = False

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
    except Exception as e:
        logging.debug(e, ": test_skeleton.py > line 72-78 > encountered while testing for pounds.")
        is_pounds = False
    try:
        int(user_input.replace('£', ''))
        is_sing_or_doub = True if not is_pennies and '£' not in user_input and not is_pounds else False
    except Exception as e:
        logging.debug(e, ": test_skeleton.py > line 79-84 > encountered while testing for single/double.")
        is_sing_or_doub = False
    is_missing_pence = True if '£' in user_input and 'p' in user_input and '.' not in user_input else False
    if is_missing_pence:
        is_pennies = is_pounds = is_pound_pence = is_sing_or_doub = is_pound_decimal = False

    user_input = user_input.replace('p', '') if is_pennies else user_input
    cur_pat = "(?:[\£\]{1}[,\d]+.?\d*)"  # regex pattern for finding currency or cash amount strings

    # coin processing mechanism
    if is_pennies:  # e.g. 123p, 4p, 167p, etc.
        temp_input = user_input.replace('p', '')
        temp_input = round(float(temp_input), 2)
        user_input = '£' + str(temp_input)
        re.search(cur_pat, user_input)[0].replace('£', '')
        print(str(copy_input), ' = ', get_coins(temp_input, signal='p')[0])
        terminal.show_result_table(  # describe coins in a terminal table
            user_input=copy_input, data=get_coins(temp_input, signal='p')[1])

    elif is_pounds or is_pound_pence:  # e.g. £1.33, 6.235p, 001.61p
        if '£' in user_input:
            temp_input = user_input.replace('£', '').replace('p', '')
            temp_input = round(float(temp_input), 2)
            '£' + str(temp_input)
            print(str(copy_input), ' = ', get_coins(temp_input, signal='£')[0])
            terminal.show_result_table(
                user_input=copy_input, data=get_coins(temp_input, signal='£')[1])
        else:  # e.g. 1.97, 10.75, 0.56, etc.
            temp_input = round(float(user_input.replace('p', '')), 2)
            print(str(copy_input), ' = ', get_coins(temp_input, signal='£')[0])
            terminal.show_result_table(
                user_input=copy_input, data=get_coins(temp_input, signal='£')[1])

    elif is_sing_or_doub:  # ...or more. # e.g. 6, 75, etc.
        print(str(copy_input), ' = ', get_coins(int(user_input), signal='p')[0])
        terminal.show_result_table(
            user_input=copy_input, data=get_coins(int(user_input), signal='p')[1])

    elif is_pound_decimal:  # e.g. £1.97p, £1.256532677p, etc.
        print(str(copy_input), ' = ', get_coins(round(float(user_input), 2), signal='£')[0])
        terminal.show_result_table(
            user_input=copy_input, data=get_coins(round(float(user_input), 2), signal='£')[1])

    elif is_missing_pence:  # e.g. £1.p, £.75p, etc.
        temp_input = round(float(user_input.replace('p', '').replace('£', '')), 2)
        print(str(copy_input), ' = ', get_coins(temp_input, signal='£')[0])
        terminal.show_result_table(user_input=copy_input, data=get_coins(temp_input, signal='£')[1])
    else:  # invalid input -> just print 0
        print(0)
    print()
