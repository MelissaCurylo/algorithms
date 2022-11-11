"""
Leetcode # 1413. Minimum Value to Get Positive Step by Step Sum

Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

Example 1:
    Input: nums = [-3,2,-3,4,2]
    Output: 5
    Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
    step by step sum
    startValue = 4 | startValue = 5 | nums
    (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
    (1 +2 ) = 3  | (2 +2 ) = 4    |   2
    (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
    (0 +4 ) = 4  | (1 +4 ) = 5    |   4
    (4 +2 ) = 6  | (5 +2 ) = 7    |   2

Example 2:
    Input: nums = [1,2]
    Output: 1
    Explanation: Minimum start value should be positive. 

Example 3:
    Input: nums = [1,-2,-3]
    Output: 5


Constraints:
    1 <= nums.length <= 100
    -100 <= nums[i] <= 100

"""

nums = [-3,2,-3,4,2]
nums1 = [1,2]
nums2 = [1,-2,-3]

# class Solution:
# def minStartValue(self, nums: list[int]) -> int:

def minStartValue(nums: list[int]) -> int:
    minimum_value = 0 
    total = 0 # use for step by step to find minimum value

    for num in nums: 
        total += num
        # print(f"this is the total: {total}") # using print for my understanding/step-through
        minimum_value = min(minimum_value, total)
        # print(f"this is the minimum value: {minimum_value}") # using print for my understanding/step-through
    
    return -minimum_value + 1 # this gives the minimum valid staring value

print(minStartValue(nums))
print(minStartValue(nums1))
print(minStartValue(nums2))

# Time Complexity = O(n)
    # Linear time because the one for loop iterates over n items at same pace and iterates only once through.

# Space Complexity = O(1) 
    # Memory used is constant and not dependent on the data processed. Only step by step is calculated to find minimum total. 




"""
Solution Notes:

- Goal: Find minimum starting value that is <= 1 while summing subarray sums.

- Using prefix[i] technique:
    1. Create and set minimum value to zero.
    2. Create and set total value to zero and use total to find/calculate updated minimum value.
        1a. Total value needs to sum equal or greater than 1. 
        1b. Value is found through intuitive approach by mathematically finding minimum total from the step by step. 
            nums = [-3,2,-3,4,2]  
            # Using: list = [a, a + b, a + b + c, a + b + c + d] with start_value = 0
                # Calculation step one: What is my minimum value?
                    # -3 + 2 = -1
                    # -1 + -3 = -4
                    # -4 + 4 = 0
                    # 0 + 2 = 2
                    --> Minimum value = -4
                # Calculation step two: What added to minimum value gets me to one?
                    # -4 + x = 1
                    # -4 + 5 = 1
                    # x = 5
                    --> 5 is the value that becomes the minimum value. 
    3. Return minimum value


- Notes:
    - Prefix concept prefix[i] is the sum of all elements up to the index i (inclusive). 
        - given nums = [5, 2 , 1, 6, 3, 8] and prefix would give prefix = [5, 7, 8, 14, 17, 25]
    Prefix tool costs O(n) to build but O(1) for using in all future subarray queries. 


- Pseudocode:
    prefix = [nums[0]]
    for i in [1, len]

"""