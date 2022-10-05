"""
Leetcode # 392 Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the 
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
        Input: s = "abc", t = "ahbgdc"
        Output: true

Example 2:
        Input: s = "axc", t = "ahbgdc"
        Output: false

Constraints:
        0 <= s.length <= 100
        0 <= t.length <= 104
        s and t consist only of lowercase English letters.


Follow up: In this scenario, how would you change your code?
    Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, 
    and you want to check one by one to see if t has its subsequence. 
            

"""

# class Solution:
def isSubsequence(s: str, t: str) -> bool:
    i = j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("abc", "ahbabc"))
print(isSubsequence("1","abc"))
print(isSubsequence("aaa","abc"))
print(isSubsequence(" ","abc")) # edgecase




"""
Using Two-pointers to solve in linear time

Time complexity: O(n)
Space complexity: O(1)

- Time complexity based on the string length of t as s is dependent on t. Worst case the entire string would need to be compared to find if
    there is a subsequence or not but still requires O(n) time.  
- Space complexity with iteration will have constant memory being consumed without regard to input. 


Follow-up Answer:
    - The target string will remain as a constant matching to each source of the incoming s strings. 
    - Following the two-point technique, upon each incoming s string scan the t string and compare.
        - This will take time and likely create bottlenecks.
    
    - After some research another data structure would be a hashmap creating key:value pairs to quickly lookup
        which s string is a match to the constant t string. Speed the algorithm up with using a 
        binary search (if sorted) and greedy match. 

    - Time complexity: O(n + m log n)
        - build hashmap = O(n)
        - binary search = O(log n)
        - searching two different strings O(n + m)
"""