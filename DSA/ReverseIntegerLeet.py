"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21


Constraints:

-231 <= x <= 231 - 1
"""

class Solution(object):
    def reverse(self, x):
        y=str(abs(x))
        y=y[::-1]
        y=int(y)
        i=1
        if y<(2**31)-1 and x>0:
            pass
        elif -y>(-(2**31)) and x<0:
            i=-1
        else:
            y=0
        return y*i