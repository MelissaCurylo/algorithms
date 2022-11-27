"""
LeetCode # 1 Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109

    Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
    
"""

nums1 = [2,7,11,15] 
target1 = 9

nums2 = [3,2,4] 
target2 = 6

nums3 = [3,3] 
target3 = 6


# Brute Force Solution 1
    # Time Complexity: O(n^2)
        # nested for loops

def bruteForce(nums, target):
    for numOne in range(len(nums)):
        for numTwo in range(numOne + 1, len(nums)):
            sum = nums[numOne] + nums[numTwo]

            if sum == target:
                return [numOne, numTwo]

print(bruteForce(nums1, target1))



# Brute Force Solution 2
    # Time Complexity: O(n^2)
        # nested for loops

def bruteForce2(nums, target):
    for numOne in range(len(nums)):
        for numTwo in range(numOne + 1, len(nums)):
            if numTwo == target - numOne:
                return [numOne, numTwo]

print(bruteForce2(nums1,target1))