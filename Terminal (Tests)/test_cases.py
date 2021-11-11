"""
* @author: Awwal Mohammed
* date: 09-11-21
* program title: test_cases.py

description:
\t This program performs 24 explicit unit tests with the standard Python Unit testing framework.
\t ALL provided test data (refer to README.md) and additional new cases are tested (test case #18+).
\t Core functionalities of the main routine are called via test_skeleton.py.
\t All test calls are invoked free of exception-handling.
\t Once you understand the program structure, feel free to add your own tests.
"""

import unittest
import test_skeleton
import sys
import io


class TestMinSterlingCoin(unittest.TestCase):
    def test_case_1(self, test_data=6, output='6  =  1 x 5p, 1 x 1p'):
        # Test Case 1, Input: 6
        old_stdout = sys.stdout                         # memorize the default stdout stream
        sys.stdout = buffer = io.StringIO()             # store initial and final stdout streams
        print(test_skeleton.main(test_data))            # make result accessible in stdout stream
        sys.stdout = old_stdout                         # put the old stream back in place
        self.assertTrue(output in buffer.getvalue())    # check if expected results is printed
        print(                                          # only prints if assertion test is passed
            f"Input: {test_data}\nExpected Results: {output}")

    def test_case_2(self, test_data=75, output='75  =  1 x 50p, 1 x 20p, 1 x 5p'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_3(self, test_data='167p', output='1 x £1, 1 x 50p, 1 x 10p, 1 x 5p, 1 x 2p'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_4(self, test_data='4p', output='4p  =  2 x 2p'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_5(self, test_data=1.97, output='1 x £1, 1 x 50p, 2 x 20p, 1 x 5p, 1 x 2p'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_6(self, test_data='£1.33', output='1 x £1, 1 x 20p, 1 x 10p, 1 x 2p, 1 x 1p'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_7(self, test_data='£2', output='1 x £2'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_8(self, test_data='£20', output='10 x £2'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_9(self, test_data='£1.97p', output='1 x £1, 1 x 50p, 2 x 20p, 1 x 5p, 1 x 2p'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_10(self, test_data='£1p', output='1 x £1'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_11(self, test_data='£1.p', output='1 x £1'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_12(self, test_data='001.61p', output='1 x £1, 1 x 50p, 1 x 10p, 1 x 1p'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_13(self, test_data='6.235p', output='3 x £2, 1 x 20p, 2 x 2p'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_14(self, test_data='£1.256532677p', output='1 x £1, 1 x 20p, 1 x 5p, 1 x 1p'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_15(self, test_data='', output='0'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        self.assertTrue(buffer.getvalue()[0] == output)
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_16(self, test_data='1x', output='0'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        self.assertTrue(buffer.getvalue()[0] == output)
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_17(self, test_data='.45', output='2 x 20p, 1 x 5p'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_18(self, test_data='£.89', output='1 x 50p, 1 x 20p, 1 x 10p, 1 x 5p, 2 x 2p'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_19(self, test_data='£1..0p', output='0'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        self.assertTrue(buffer.getvalue()[0] == output)
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_20(self, test_data='..p', output='0'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        self.assertTrue(buffer.getvalue()[0] == output)
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_21(self, test_data='AxY', output='0'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        self.assertTrue(buffer.getvalue()[0] == output)
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_22(self, test_data='*_/+-', output='0'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        self.assertTrue(buffer.getvalue()[0] == output)
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_23(self, test_data='£1x.0p', output='0'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        self.assertTrue(buffer.getvalue()[0] == output)
        print(f"Input: {test_data}\nExpected Results: {output}")

    def test_case_24(self, test_data='£p', output='0'):
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(test_skeleton.main(test_data))
        sys.stdout = old_stdout
        self.assertTrue(output in buffer.getvalue())
        self.assertTrue(buffer.getvalue()[0] == output)
        print(f"Input: {test_data}\nExpected Results: {output}")


if __name__ == '__main__':
    unittest.main()
