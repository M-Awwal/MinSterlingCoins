"""
* @author: Awwal Mohammed
* date: 09-11-21
* program title: test_skeleton.py

description:
\t This program holds the structure for methods being called by test_cases.py,
\t which in turn performs individual explicit tests based on
\t the provided test data (refer to README.md).
\t As you'll see, this source file contains segments of code identical to main_routine.py.
\t Elaborate comments are ignored, but can be referenced from main_routine.py.

"""

import re
import test_terminal_graphics
from test_utils import MinSterlingUtils

terminal = test_terminal_graphics.MinSterlingTerminal()


def main(data):
    # priliminary filtering
    user_input = data.__str__().lower()
    copy_input = user_input

    # validate user input and obtain a series of boolean signals
    validations = MinSterlingUtils.validate_input(user_input=user_input)
    is_pennies, is_pounds, is_pound_pence, is_sing_or_doub, is_pound_decimal, \
        is_missing_pence, is_sing_dig_pound = tuple(validations.values())

    user_input = user_input.replace('p', '') if is_pennies else user_input
    cur_pat = "(?:[\£\]{1}[,\d]+.?\d*)"

    try:  # coin processing mechanism
        if is_pennies:  # e.g. 123p, 4p, 167p, etc.
            temp_input = user_input.replace('p', '')
            temp_input = round(float(temp_input), 2)
            user_input = '£' + str(temp_input)
            amount = re.search(cur_pat, user_input)[0].replace('£', '')
            min_coins = MinSterlingUtils.get_coins(temp_input, signal='p')  # calculate coins needed
            print(str(copy_input), ' = ', min_coins[0])  # print one line string of results
            return terminal.show_result_table(user_input=copy_input, data=min_coins[1])  # tabluate results

        elif is_pounds or is_pound_pence:  # e.g. £1.33, 6.235p, 001.61p
            if '£' in user_input and user_input.count('£') <= 1:
                temp_input = user_input.replace('£', '').replace('p', '')
                temp_input = round(float(temp_input), 2)
                user_input = '£' + str(temp_input)
                amount = re.search(cur_pat, user_input)[0]
                min_coins = MinSterlingUtils.get_coins(temp_input, signal='£')
                print(str(copy_input), ' = ', min_coins[0])
                return terminal.show_result_table(user_input=copy_input, data=min_coins[1])
            else:  # e.g. 1.97, 10.75, 0.56, etc.
                temp_input = round(float(user_input.replace('p', '')), 2)
                min_coins = MinSterlingUtils.get_coins(temp_input, signal='£')
                print(str(copy_input), ' = ', min_coins[0])
                return terminal.show_result_table(user_input=copy_input, data=min_coins[1])

        elif is_sing_or_doub:  # ...or more. # e.g. 6, 75, 139, etc.
            cur_val = int(user_input)
            min_coins = MinSterlingUtils.get_coins(cur_val, signal='p')
            print(str(copy_input), ' = ', min_coins[0])
            return terminal.show_result_table(user_input=copy_input, data=min_coins[1])

        elif is_pound_decimal and user_input.count('£') <= 1:  # e.g. £1.97p, £1.256532677p, £0.25p, etc.
            cur_val = round(float(user_input), 2)
            min_coins = MinSterlingUtils.get_coins(cur_val, signal='£')
            print(str(copy_input), ' = ', min_coins[0])
            return terminal.show_result_table(user_input=copy_input, data=min_coins[1])

        elif is_missing_pence and user_input.count('£') <= 1:  # e.g. £1.p, £.75p, etc.
            temp_input = round(float(user_input.replace('p', '').replace('£', '')), 2)
            min_coins = MinSterlingUtils.get_coins(temp_input, signal='£')
            print(str(copy_input), ' = ', min_coins[0])
            return terminal.show_result_table(user_input=copy_input, data=min_coins[1])

        return print(0)  # invalid input -> just print 0
    except Exception:
        print(0)  # caught exception -> just print 0
