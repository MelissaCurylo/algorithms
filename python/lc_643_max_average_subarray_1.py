"""
LeetCode # 643 Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 

Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
    Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
    Input: nums = [5], k = 1
    Output: 5.00000

Constraints:
    n == nums.length
    1 <= k <= n <= 105
    -104 <= nums[i] <= 104
"""

nums = [1,12,-5,-6,50,3]
k = 4

# class Solution:
#     def findMaxAverage(self, nums: list[int], k: int) -> float:

def findMaxAverage(nums: list[int], k: int) -> float:
    subarray = sum(nums[:k]) # creating window to range of k constraint.
    maxAverage = subarray

    for i in range(k, len(nums)):
        subarray += (nums[i] - nums[i - k]) # updating pointers and sliding window.
        
        if maxAverage < subarray:
            maxAverage = subarray
    return maxAverage / k

print(findMaxAverage(nums, k))

"""
Time complexity: O(n)
    - At most will visit an index position twice and iterating left to right. 

Space complexity: O(1) 
    - Temporary storage for values. 
"""

"""
Pseudocode:

- Goal: Return the max average value of a contiguous subarray with length that is equal to k's value.

- Using Sliding Window technique:
    1. Assign two pointers, left and right at zero index.
    2. Need two variables:
        - subarray creates the window range per k constraints.
        - maxAverage set to subarray value which will hold the sum of window 
    3. Iterate through window via for loop with bounds of array length to k constraint.

    4. Update the current value of window through each iteration.
        -   Window length must be equal to k value at all times. 
    5. Compare maxAverage holding previous window value to subarray with new window value.
        - If maxAverage is less than subarray then maxAverage will be set to subarray value. 
    6. Return average of maxAverage divided by k. 
"""