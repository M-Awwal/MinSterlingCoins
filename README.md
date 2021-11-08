# Minimum Sterling Coins and Pennies Evaluator

### The minimum coin problem (with a twist!)

A simple repo for a program such that given a number of pennies, will calculate the minimum number of Sterling coins equivalent to that amount.

#### How it works

This version of the minimum coin problem processes the following Sterling coins and Pennies:

<table border="0">
 <tr>
    <td>£2</td>
    <td>£1</td>
    <td>50p</td>
    <td>20p</td>
 </tr>
 <tr>
    <td>10p</td>
    <td>5p</td>
    <td>2p</td>
    <td>1p</td>
 </tr>
</table>

The evaluation process begins with basic filtering to account for input validation. This is subsequently followed by a bit of dynamic programming where the input is parsed through a top-down divisional minimization, starting with the highest coin.

The result is returned in a string (iterated and concatenated from a dictionary counter) describing the minimum number of coins used, based on the given input.

