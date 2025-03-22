"""
Given a number n, find the smallest number that has the same set of digits as n and is greater than n. If n is the greatest possible number with its set of digits, report it.

Example 1:

Input:
N = 143
Output: 314
Explanation: Numbers possible with digits
1, 3 and 4 are: 134, 143, 314, 341, 413, 431.
The first greater number after 143 is 314.
Example 2:

Input:
N = 431
Output: not possible
Explanation: Numbers possible with digits
1, 3 and 4 are: 134, 143, 314, 341, 413, 431.
Clearly, there's no number greater than 431.

"""

class Solution:
    def findNext (self,n):
    