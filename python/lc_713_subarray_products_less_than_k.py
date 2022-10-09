"""

713. Subarray Product Less Than K

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:
    Input: nums = [10,5,2,6], k = 100
    Output: 8

    Explanation: The 8 subarrays that have product less than 100 are:  [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

    Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:
    Input: nums = [1,2,3], k = 0
    Output: 0

Constraints:
    1 <= nums.length <= 3 * 104
    1 <= nums[i] <= 1000
    0 <= k <= 106

"""

"""
# Working it out my logic:

- Product = multiplication.
- Contiguous subarray = connected index positions.
- Product of subarray constraint = less than k.
- Current index max subarray value: right pointer - left pointer + 1
    - How many valid subarrays could end at limiting bound index after each iteration? 

Input: nums = [10,5,2,6], k = 100

# Wording it out full logic:
- Index pointers start at index 0.
    - Product of index 0 = 10
    - Subarray = 1
- Right pointer moves to index 1.
    - Product of both index 0 and 1 = [10] * [5] = 50
    - Product is less than k = 100
    - Subarray = 2
- Right pointer moves to index 2.
    - Product of index 0, 1, and 2 = [10] * [5] * [2] = 100
    - Product exceeds constraint: 100 !< 100
- Left pointer moves to index 1.
    - Product of index 1 and 2 = [5] * [2] = 10
    - Product within in constraints: 10 < 100
    - Subarray = 2
- Right pointer moves to index 3.
    - Product of index 5,2,6 = [5] * [2] * [6] = 60
    - Subarray = 3
- All subarrays = [10], [5], [10,5], [2], [5,2], [5,2,6], [2,6], [6]
- Summation of all subarrays = 1+2+2=3 = 8 

"""

from re import sub


nums = [10,5,2,6]
k = 100

# nums = [1,2,3]
# k = 0

# class Solution:
#     def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:

def numSubarrayProductLessThanK(nums, k):

    left = 0
    subarray_total = 0
    current_value = 1

    for right in range (len(nums)):
        current_value *= nums[right]

        while left <= right and current_value >= k:
            current_value //= nums[left]
            left += 1

        subarray_total += right - left + 1

    return subarray_total

print(numSubarrayProductLessThanK(nums,k))

"""
Pseudocode:

- Goal: find max subarray amount via multiplication and each must rest below constraint k.

- Using Sliding Window technique:
    1. Assign two pointers, left and right at zero index.
    2. Need variables to store 
        - subarray total
        - current index window
            - Current index value needs to begin at 1 as multiplying 0 would always result in 0.
    3. Need a way to iterate array - for loop with bounds of array length.
    4. Update the current value with window through each iteration.
    5. Need to set a condition to evaluate the k constraint to current value:
        - while loop
    6. Update subarray total and return.


"""