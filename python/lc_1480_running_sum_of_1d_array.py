"""
1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.


Example 1:
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
    Input: nums = [1,1,1,1,1]
    Output: [1,2,3,4,5]
    Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
    Input: nums = [3,1,2,10,1]
    Output: [3,4,6,16,17]


Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""




nums1 = [1,2,3,4]
nums2 = [1,1,1,1,1]
nums3 = [3,1,2,10,1]


# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:

def runningSum(nums: list[int]) -> list[int]:

    result = []
    current_value = 0

    for num in nums:
        current_value += num
        result.append(current_value)

    return result

print(runningSum(nums1))
print(runningSum(nums2))
print(runningSum(nums3))

# Time Complexity: O(n) 
    # Linear time due to n being elements in input array receiving the same number of operations on each element. 
    # Only one for loop with one pass through needed to traverse the array. 

# Space Complexity: O(n)
    # Linear time due to storing the same amount of elements as the initial starting value.

"""
Pseudocode: Solution

- Goal: Obtain running total (addition) of all listed numbers in array. 

- Using Sliding Window technique:
    1. Create a new array to store running values.
    2. Create a variable to store the current index value.
    2. Create for loop condition:
        - Take current value and add to index number at current position
        - Append current value to the new array
    3. Return rew array with new results.
    

    Notes:
    - Not contingent to order but if the array list was out of order I'd attempt this solutin with two pointers iterating from opposite ends.
        - Each pointer would add element in index then compare positions and only store the largest value moving to the smallest values. 

"""