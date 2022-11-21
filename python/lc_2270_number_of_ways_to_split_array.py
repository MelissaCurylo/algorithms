"""
LeetCode # 2270. Number of Ways to Split Array

You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.


Example 1:
    Input: nums = [10,4,-8,7]
    Output: 2

    Explanation: There are three ways of splitting nums into two non-empty parts:
        - Split nums at index 0. Then, the first part is [10], and its sum is 10. The second part is [4,-8,7], and its sum is 3. Since 10 >= 3, i = 0 is a valid split.
        - Split nums at index 1. Then, the first part is [10,4], and its sum is 14. The second part is [-8,7], and its sum is -1. Since 14 >= -1, i = 1 is a valid split.
        - Split nums at index 2. Then, the first part is [10,4,-8], and its sum is 6. The second part is [7], and its sum is 7. Since 6 < 7, i = 2 is not a valid split.
        Thus, the number of valid splits in nums is 2.

Example 2:
    Input: nums = [2,3,1,0]
    Output: 2

    Explanation: There are two valid splits in nums:
        - Split nums at index 1. Then, the first part is [2,3], and its sum is 5. The second part is [1,0], and its sum is 1. Since 5 >= 1, i = 1 is a valid split. 
        - Split nums at index 2. Then, the first part is [2,3,1], and its sum is 6. The second part is [0], and its sum is 0. Since 6 >= 0, i = 2 is a valid split.

Constraints:
    2 <= nums.length <= 105
    -105 <= nums[i] <= 105


Hint: For any index i, how can we find the sum of the first (i+1) elements from the sum of the first i elements?
Hint: If the total sum of the array is known, how can we check if the sum of the first (i+1) elements greater than or equal to the remaining elements?
"""

nums1 = [10,4,-8,7]
nums2 = [2,3,1,0]

# class Solution:
#     def waysToSplitArray(self, nums: list[int]) -> int:

def waysToSplitArray(nums: list[int]) -> int:

    answer = 0    
    left_prefix = 0
    total_prefix = sum(nums)

    for number in range(len(nums) - 1):
        left_prefix += nums[number]
        right_prefix = total_prefix - left_prefix

        if left_prefix >= right_prefix:
            answer += 1

    return answer

print(waysToSplitArray(nums1))
print(waysToSplitArray(nums2))

# Time Complexity: O(n) 
    # Linear time due to n being elements in input array receiving the same number of operations on each element. 
    # Only one for loop with one pass through needed to traverse the array. 

# Space Complexity: O(1)
    # Constant time as did not go with recreating the array and stored values in variables instead. 
    # If recreating an array to store the values time complexity would increse to O(n).

"""
Pseudocode/Solution:

- Goal: Find total valid splits of the array via prefix sums and sliding window techniques. 

- Using Prefix Sum and Sliding Window technique:
    1. Create three variables:
        - answer to update total of prefix windows.
        - left prefix to store values.
        - total prefix to use for calculating difference. Store the sum of the entire array in total prefix.
    2. Create for loop condition with bounds:
        - Take current value of left prefix and add to index number at current position.
        - Set right prefix to the total prefix minus the left. 
            - This will guarantee that slot is reserved to the right having at least one element. 
    3. Set if  condition to determine if window of prefix is valid and counts as a split.
        - As long as left prefix is greater/equal to right prefix add one to the total splits.
    4. Return total split amount.
    

    Notes:
    - Keep track of left and right prefix totals when moving "window".
    - Must have at least one element at the end (right side). ("one element to the right of i")
    - Only need the sums of the edges both left and right. No need to store an array, instead store values in variables.

"""