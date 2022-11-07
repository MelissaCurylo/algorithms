"""
LeetCode # 1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
    Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6
    Explanation: [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is from index 5 thru index 10.

Example 2:
    Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    Output: 10
    Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is from index 2 thru index 11.


Constraints:
    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
    0 <= k <= nums.length

"""


nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

# Soltuion version # 1
def longestOnes(nums: list[int], k: int) -> int:          
    
    left_pointer = 0
    right_pointer = 0


    while ( right_pointer < len(nums)):

        if nums[right_pointer] == 0:
            k -= 1
        if k < 0:
            if nums[left_pointer] == 0:
                k += 1
            left_pointer += 1
        right_pointer += 1
    return right_pointer - left_pointer

print(longestOnes(nums,k))



# Solution version # 2
# def longestOnes(nums: list[int], k: int) -> int:

#     left_pointer = 0

#     for right_pointer in range(len(nums)):

#         k -= 1 - nums[right_pointer]

#         if k < 0: 
#             k += 1 - nums[left_pointer]
#             left_pointer += 1
#     return right_pointer - left_pointer + 1

# print(longestOnes(nums,k))


"""
Pseudocode: Solution # 1

- Goal: Return the longest contiguous subarray containing only 1's.

- Using Sliding Window technique:
    1. Assign two pointers, left and right at zero index.
    3. Iterate with right pointer until k valued number of zeros is consumed. [0,k]
    4. Update the current value of windows through each iteration.
    5. Maintain window size and move left pointer only when k is less than zero. 
    6. Max ones subarray will be right subtracted from left pointer then add one to account for index positions starting at zero. 
    7. Compare max length holding previous window value to subarray with new window value. 
    8. Return max length of ones. 



    Notes:
    - Flipping 0's can only occur if the 0 extends the existing window of 1's. 
    - In any one window there cannot be greater than k zeros.
    - Window is not fixed to allow growing and shrinking for finding the longest subarray of 1's.
        - In that case, may not need to actually flip any zeros
    - Sliding window technique with two pointers: 
        - right pointer responsible for expanding window and left pointer responsible for contraction when needed. 
        - only one pointer moves at any given time unless k zeros are used up. 
        - Expand window with right pointer until the k limited range of 0's [0,k] is reached then record longest window.  
"""