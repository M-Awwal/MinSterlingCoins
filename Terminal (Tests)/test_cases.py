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

try:  # Test Case 1, Input: 6
    test_skeleton.main(6)
    print(f"Test Case 1 Passed, Input: {6}")
except Exception as e:
    logging.debug(e)
    logging.info(e)

try:  # Test Case 2, Input: 75
    test_skeleton.main(75)
    print(f"Test Case 2 Passed, Input: {75}")
except Exception as e:
    logging.debug(e)
    logging.info(e)

try:  # Test Case 3, Input: 167p
    test_skeleton.main('167p')
    print(f"Test Case 3 Passed, Input: {'167p'}")
except Exception as e:
    logging.debug(e)
    logging.info(e)

try:  # Test Case 4, Input: 4p
    test_skeleton.main('4p')
    print(f"Test Case 4 Passed, Input: {'4p'}")
except Exception as e:
    logging.debug(e)
    logging.info(e)

try:  # Test Case 5, Input: 1.97
    test_skeleton.main(1.97)
    print(f"Test Case 5 Passed, Input: {1.97}")
except Exception as e:
    logging.debug(e)
    logging.info(e)

try:  # Test Case 6, Input: £1.33
    test_skeleton.main('£1.33')
    print(f"Test Case 6 Passed, Input: {'£1.33'}")
except Exception as e:
    logging.debug(e)
    logging.info(e)

try:  # Test Case 7, Input: £2
    test_skeleton.main('£2')
    print(f"Test Case 7 Passed, Input: {'£2'}")
except Exception as e:
    logging.debug(e)
    logging.info(e)

try:  # Test Case 8, Input: £20
    test_skeleton.main('£20')
    print(f"Test Case 8 Passed, Input: {'£20'}")
except Exception as e:
    logging.debug(e)
    logging.info(e)

try:  # Test Case 9, Input: £1.97p
    test_skeleton.main('£1.97p')
    print(f"Test Case 9 Passed, Input: {'£1.97p'}")
except Exception as e:
    logging.debug(e)
    logging.info(e)

try:  # Test Case 10, Input: £1p
    test_skeleton.main('£1p')
    print(f"Test Case 10 Passed, Input: {'£1p'}")
except Exception as e:
    logging.debug(e)
    logging.info(e)

try:  # Test Case 11, Input: £1.p
    test_skeleton.main('£1.p')
    print(f"Test Case 11 Passed, Input: {'£1.p'}")
except Exception as e:
    logging.debug(e)
    logging.info(e)

try:  # Test Case 12, Input: 001.61p
    test_skeleton.main('001.61p')
    print(f"Test Case 12 Passed, Input: {'001.61.p'}")
except Exception as e:
    logging.debug(e)
    logging.info(e)

try:  # Test Case 13, Input: 6.235p
    test_skeleton.main('6.235p')
    print(f"Test Case 13 Passed, Input: {'6.235.p'}")
except Exception as e:
    logging.debug(e)
    logging.info(e)

try:  # Test Case 14, Input: £1.256532677p
    test_skeleton.main('£1.256532677p')
    print(f"Test Case 14 Passed, Input: {'£1.256532677p'}")
except Exception as e:
    logging.debug(e)
    logging.info(e)

try:  # Test Case 15, Input:
    test_skeleton.main('')
    print(f"Test Case 15 Passed, Input: {''}")
except Exception as e:
    logging.debug(e)
    logging.info(e)

try:  # Test Case 16, Input: 1x
    test_skeleton.main('1x')
    print(f"Test Case 16 Passed, Input: {'1x'}")
except Exception as e:
    logging.debug(e)
    logging.info(e)

try:  # Test Case 17, Input: £1x.0p
    test_skeleton.main('£1x.0p')
    print(f"Test Case 17 Passed, Input: {'£1x.0p'}")
except Exception as e:
    logging.debug(e)
    logging.info(e)

try:  # Test Case 18, Input: £p
    test_skeleton.main('£p')
    print(f"Test Case 18 Passed, Input: {'£p'}")
except Exception as e:
    logging.debug(e)
    logging.info(e)
