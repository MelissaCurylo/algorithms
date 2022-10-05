"""
Write a function that reverse a string. The input string is given as an array of characters 's'.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Example 2:
    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]


Constraints:
    1 <= s.length <= 105
    s[i] is a printable ascii character.
"""


s = ["h","e","l","l","o"]
s = ["M","e","l","i","s","s","a"]

# class Solution:
#     def reverseString(self, s: list[str]) -> None:
def reverseString(s: list[str]):
        i = 0
        j = len(s)-1
        
        while i < j:
            s[i], s[j] = s[j], s[i]
            
            i += 1
            j -= 1
            
        return s
        
        
        
        """
            Using Two-pointer technique
                1. Create two pointers
                    1a. one pointer at index 0
                    1b. another at the end of the list index
                2. Iterate both pointers over the array index values 
                    2a. swap each value at each iteration
                    2b. iterate until the pointers meet and can do no further iterations
                3. return
        """