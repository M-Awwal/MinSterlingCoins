"""
* @author: Awwal Mohammed
* date: 09-11-21
* program title: test_cases.py

description:
\t This program performs individual explicit tests based on the provided test data (refer to README.md).
\t We call the core functionalities of the main routine in an encapsulated manner, via test_skeleton.py.
\t We perform all test calls free of `strong` exception-handling,
\t we utilize the said error catching mechanism here for purely debugging purposes.\n
\t Once you understand the program structure, feel free to add your own tests.

"""
import logging
import test_skeleton

# the debugger is stubborn and will ocassionally refuse to output tracebacks
# this line reduces the debugging level (set by default to WARN [or NOTSET])
# so that it doesn't ignore anything below INFO level, more: https://stackoverflow.com/a/57234760
# in case debugger refuses to output traceback (like it often does),
# ensure to import sys and traceback, then use: traceback.print_exception(*sys.exc_info())
logging.basicConfig(level=logging.INFO)

try:  # Test Case 1, Input: 6
    test_skeleton.main(6)
    print(f"Test Case 1 Passed, Input: {6}")
except Exception as e:
    logging.info(msg='Test Case 1: Input: 6', exc_info=e)

try:  # Test Case 2, Input: 75
    test_skeleton.main(75)
    print(f"Test Case 2 Passed, Input: {75}")
except Exception as e:
    logging.info(msg='Test Case 2: Input: 75', exc_info=e)

try:  # Test Case 3, Input: 167p
    test_skeleton.main('167p')
    print(f"Test Case 3 Passed, Input: {'167p'}")
except Exception as e:
    logging.info(msg='Test Case 3: Input: 167p', exc_info=e)

try:  # Test Case 4, Input: 4p
    test_skeleton.main('4p')
    print(f"Test Case 4 Passed, Input: {'4p'}")
except Exception as e:
    logging.info(msg='Test Case 4: Input: 4p', exc_info=e)

try:  # Test Case 5, Input: 1.97
    test_skeleton.main(1.97)
    print(f"Test Case 5 Passed, Input: {1.97}")
except Exception as e:
    logging.info(msg='Test Case 5: Input: 1.97', exc_info=e)

try:  # Test Case 6, Input: £1.33
    test_skeleton.main('£1.33')
    print(f"Test Case 6 Passed, Input: {'£1.33'}")
except Exception as e:
    logging.info(msg='Test Case 6: Input: £1.33', exc_info=e)

try:  # Test Case 7, Input: £2
    test_skeleton.main('£2')
    print(f"Test Case 7 Passed, Input: {'£2'}")
except Exception as e:
    logging.info(msg='Test Case 7: Input: £2', exc_info=e)

try:  # Test Case 8, Input: £20
    test_skeleton.main('£20')
    print(f"Test Case 8 Passed, Input: {'£20'}")
except Exception as e:
    logging.info(msg='Test Case 8: Input: £20', exc_info=e)

try:  # Test Case 9, Input: £1.97p
    test_skeleton.main('£1.97p')
    print(f"Test Case 9 Passed, Input: {'£1.97p'}")
except Exception as e:
    logging.info(msg='Test Case 9: Input: £1.97p', exc_info=e)

try:  # Test Case 10, Input: £1p
    test_skeleton.main('£1p')
    print(f"Test Case 10 Passed, Input: {'£1p'}")
except Exception as e:
    logging.info(msg='Test Case 10: Input: £1p', exc_info=e)

try:  # Test Case 11, Input: £1.p
    test_skeleton.main('£1.p')
    print(f"Test Case 11 Passed, Input: {'£1.p'}")
except Exception as e:
    logging.info(msg='Test Case 11: Input: £1.p', exc_info=e)

try:  # Test Case 12, Input: 001.61p
    test_skeleton.main('001.61p')
    print(f"Test Case 12 Passed, Input: {'001.61p'}")
except Exception as e:
    logging.info(msg='Test Case 12: Input: 001.61p', exc_info=e)

try:  # Test Case 13, Input: 6.235p
    test_skeleton.main('6.235p')
    print(f"Test Case 13 Passed, Input: {'6.235.p'}")
except Exception as e:
    logging.info(msg='Test Case 13: Input: 6.235p', exc_info=e)

try:  # Test Case 14, Input: £1.256532677p
    test_skeleton.main('£1.256532677p')
    print(f"Test Case 14 Passed, Input: {'£1.256532677p'}")
except Exception as e:
    logging.info(msg='Test Case 14: Input: £1.256532677p', exc_info=e)

try:  # Test Case 15, Input:
    test_skeleton.main('')
    print(f"Test Case 15 Passed, Input: {''}")
except Exception as e:
    logging.info(msg='Test Case 15: Input: ', exc_info=e)

try:  # Test Case 16, Input: 1x
    test_skeleton.main('1x')
    print(f"Test Case 16 Passed, Input: {'1x'}")
except Exception as e:
    logging.info(msg='Test Case 16: Input: 1x', exc_info=e)

try:  # Test Case 17, Additional Test Input: .45
    test_skeleton.main('.45')
    print(f"Test Case 17 Passed, Input: {'.45'}")
except Exception as e:
    logging.info(msg='Test Case 17: Input: .45', exc_info=e)

try:  # Test Case 18, Additional Test Input: £.89
    test_skeleton.main('£.89')
    print(f"Test Case 18 Passed, Input: {'£.89'}")
except Exception as e:
    logging.info(msg='Test Case 18: Input: £.89', exc_info=e)

try:  # Test Case 19, Invalid Input: £1..0p
    test_skeleton.main('£1..0p')
    print(f"Test Case 19 Passed, Invalid Input: {'£1..0p'}")
except Exception as e:
    logging.info(msg='Test Case 19: Input: £1..0p', exc_info=e)

try:  # Test Case 20, Invalid Input: ..p
    test_skeleton.main('..p')
    print(f"Test Case 20 Passed, Invalid Input: {'..p'}")
except Exception as e:
    logging.info(msg='Test Case 20: Input: ..p', exc_info=e)

try:  # Test Case 21, Invalid Input: AxY
    test_skeleton.main('AxY')
    print(f"Test Case 21 Passed, Invalid Input: {'AxY'}")
except Exception as e:
    logging.info(msg='Test Case 21: Input: AxY', exc_info=e)

try:  # Test Case 22, Invalid Input: *_/+-
    test_skeleton.main('*_/+-')
    print(f"Test Case 22 Passed, Invalid Input: {'*_/+-'}")
except Exception as e:
    logging.info(msg='Test Case 22: Input: *_/+-', exc_info=e)

try:  # Test Case 23, Invalid Input: £1x.0p
    test_skeleton.main('£1x.0p')
    print(f"Test Case 23 Passed via Caught Exception, Invalid Input: {'£1x.0p'}")
except Exception as e:
    logging.info(msg='Test Case 23: Input: £1x.0p', exc_info=e)

try:  # Test Case 24, Invalid Input: £p
    test_skeleton.main('£p')
    print(f"Test Case 24 Passed via Caught Exception, Invalid Input: {'£p'}")
except Exception as e:
    logging.info(msg='Test Case 24: Input: £p', exc_info=e)
