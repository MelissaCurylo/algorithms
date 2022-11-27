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

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
def twoSum(nums: list[int], target: int) -> list[int]:
    
    newMap = {} # val : index

    for numOne, numTwo in enumerate(nums):
        current_value = target - numTwo
        if current_value in newMap:
            return [newMap[current_value], numOne]
        newMap[numTwo] = numOne

    return

print(twoSum(nums1, target1))
print(twoSum(nums2, target2))
print(twoSum(nums3, target3))




# Time Complexity: O(n) 
    # Linear time due to n being elements in input array receiving the same number of operations on each element. 
    # Only one for loop with one pass through needed to traverse the array. 

# Space Complexity: O(n)
    # Using memory by 

"""
Pseudocode/Solution:

- Goal: Find target value with only two valid index positions using Hash Map data structure. 

- Using Hash Map:
    1. Create three variables:
        - Empty hash map
        - current_value
    2. Iterate through list and locate the complement that equates target.
        - current_value + x = target
    

    Notes:
    - Math -> current_value + x = target
        - x = target - current_value
    - Map value to index. 
    - Cannot use the same index twice.
    - Incorporating enumerate() 
        - enumerate() converts data object and returns and object via adding iterating counter value to object. 
        - removes the need to instantiate i = 0.
        - enumerate starts at zero by default.


    Hash Map View nums1
    value : index
    -------------
    2   :  0
    7   :  1
    11  :  2
    15  :  3


    Hash Map View nums2
    value : index
    -------------
    3   :  0
    2   :  1
    4   :  2
    
"""

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
            if nums[numTwo] == target - nums[numOne]:
                return [numOne, numTwo]
                

print(bruteForce2(nums1,target1))
print(bruteForce2(nums2,target2))