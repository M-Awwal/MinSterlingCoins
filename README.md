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

#### How to Run

* From the ```Terminal``` directory, execute the ```main_routine.py``` file.
* The program should display the following in a console/terminal:
    * ```commandline 
      ENTER PENNIES (e.g. £2, £1, 50p, 20p, 10p, 5p, 2p and 1p):```
* Given the following input (£14.83), the corresponding output is produced:
  * ```commandline 
      ENTER PENNIES (e.g. £2, £1, 50p, 20p, 10p, 5p, 2p and 1p):
      £14.83  
      >>> £14.83 =  7 x £2, 1 x 50p, 1 x 20p, 1 x 10p, 1 x 2p, 1 x 1p
    ```

#### Test Data

In the first column is a string of user input, 
and in the second the desired integer expressed as pence.

<table border="0">
 <tr>
    <th>Input</th>
    <th>Pence Description</th>
 </tr>
 <tr>
    <td>6</td>
    <td>6 Single digit</td>
 </tr>
 <tr>
    <td>75</td>
    <td>75 Double digit</td>
 </tr>
<tr>
<td>167p</td>
<td>167 Pence symbol</td>
</tr>
 <tr>
    <td>4p</td>
    <td>4 Pence symbol single digit</td>
 </tr>
 <tr>
    <td>1.97</td>
    <td>197 Pounds decimal</td>
 </tr>
 <tr>
    <td>£1.33</td>
    <td>133 Pound symbol decimal</td>
 </tr>
 <tr>
    <td>£2</td>
    <td>200 Single digit pound symbol</td>
 </tr>
 <tr aria-rowspan="3">
    <td>£20</td>
    <td>2000 Double digit pound symbol</td>
 </tr>
 <tr>
    <td>£1.97p</td>
    <td>197 Pound & pence symbol</td>
 </tr>
 <tr>
    <td>£1p</td>
    <td>Decimal 100 missing pence</td>
 </tr>
 <tr>
    <td>£1.p</td>
    <td>100 Missing pence, Decimal point present</td>
 </tr>
 <tr>
    <td>001.61p</td>
    <td>161 Buffered zeroes</td>
 </tr>
 <tr>
    <td>6.235p</td>
    <td>624 Rounding with pence symbol</td>
 </tr>
 <tr>
    <td>£1.256532677p</td>
    <td>126 Rounding with pound and pence symbols.</td>
 </tr>

</table>

Likewise, the application should not accept the following inputs

<table border="0">
 <tr>
    <th>Input</th>
    <th>Pence</th>
    <th>Description</th>
 </tr>
 <tr>
    <td></td>
    <td>0</td>
    <td>Empty string</td>
 </tr>
 <tr>
    <td>1x</td>
    <td>0</td>
    <td>Non-numeric, non-symbol character</td>
 </tr>
 <tr>
    <td>£1x.0p</td>
    <td>0</td>
    <td>Non-numeric, non-symbol character along with valid symbols</td>
 </tr>
 <tr>
    <td>£p</td>
    <td>0</td>
    <td>Missing digits</td>
 </tr>
</table>