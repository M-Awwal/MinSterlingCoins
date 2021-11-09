"""
* @author: Awwal Mohammed
* date: 09-11-21
* program title: test_cases.py

description:
\t This program performs individual explicit tests based on the provided test data (refer to README.md).
\t We call the core functionalities of the main routine in an encapsulated manner, via test_skeleton.py.
\t We perform all test calls free of `strong` exception-handling,
\t we utilize the said error catching mechanism here for purely debugging purposes.

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






