"""
LeetCode # 977 Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1: 
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].

Example 2:
    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.


Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""

nums = [-4,-1,0,3,10]
nums1 = [-7,-3,2,3,11]

# class Solution:
#     def sortedSquares(self, nums: list[int]) -> list[int]:
def sortedSquares(nums: list[int]) -> list[int]:

    result = []

    length = len(nums)
    left_pointer = 0 
    right_pointer = length - 1

    while left_pointer <= right_pointer:
        if nums[left_pointer] * nums[left_pointer] > nums[right_pointer] * nums[right_pointer]:
            result.append(nums[left_pointer] * nums[left_pointer])
            left_pointer += 1
        else:
            result.append(nums[right_pointer] * nums[right_pointer])
            right_pointer -= 1

    return result[::-1] # returns the reverse of the array

print(sortedSquares(nums))
print(sortedSquares(nums1))


# Time Complexity: O(n)
    # Linear time due to n being elements in input array receiving the same number of operations on each element. 
    # Only one pass through array was needed when starting with the larger elements and sorting from largest to smallest. 
    # O(log n) would be to square each value then sort leading to several passes through the array. 

# Space Complexity: O(1)
    # Constant space 

"""
Pseudocode: Solution # 1

- Goal: Square each index value and return the squared values in non-decreasing order in O(n).

- Using Sliding Window technique:
    1. Create a variable to store resulting array.
    2. Create left and right pointers to iterate array.
    3. Set while condition to create boundaries for left and right pointers.
    4. Inside while condition set if condition:
        - Append the result to the new array based in if condition.
        - if left pointer squared is larger than right pointer append, store, then iterate left pointer.
        - otherwise right is greater than left pointer to append, store, then iterate right pointer.
    4. Return result by reversing it as the current condidion is in the wrong order of ascending (greatest to least) values.
    

    Notes:
    - O(log n) is established by squaring each index value then traversing the array several times to sort the array.
    - The need to traverse the array several times causes an influx in time resulting in O(log n).

"""