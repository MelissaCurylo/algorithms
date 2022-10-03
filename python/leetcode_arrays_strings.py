"""
1. Understanding Two-Pointers

Find the pair whose sum equals 10 from the sorted array 'arr':

arr = [-30, -22, -19, -16, 3, 5, 12, 17, 26, 30]

Pseudocode:

function fn(arr):
    left = 0
    right = arr.length - 1

    while left < right:
        Do some logic here depending on the problem
        Do some more logic here to decide on one of the following:
            1. left++
            2. right--
            3. Both left++ and right--


Time complexity: O(1) linear time

- While loop in this technique will never have more than O(n) iterations.
- Keep run/work inside each iteration maintains O(1) runtime. 

"""


"""
1. Return True if a given string is a palindrome, false otherwise.

- A string is considered a palindrome if it reads the same forwards and backwards.  
    - After reversing the string it reads the same before it was reversed.

Time complexity: 

"""

def check_if_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(check_if_palindrome("aba"))
print(check_if_palindrome("bba"))




"""
2. Given a sorted array of unique integers and a target intenger, return true if there 
    exists a pair of numbers that sum to target, false otherwise.

nums = [1, 2, 4, 6, 8, 9, 14, 15]

target = 13

- Brute force requires to iterate each index and would result in a time complexity of O(n^2)
- Two-pointer is better because it improves time complexity to O(n):
    - Looking at first number and last number to gather their sum and iterate through doing the same
        process until a match is found for the target number.
    - Iteration continues via while loop until while loop flipped by boolean to False.
        - Which means we've found target.

"""

nums = [1, 2, 4, 6, 8, 9, 14, 15]

def check_for_target( nums, target):
    left = 0 
    right = len(nums) - 1

    while left < right:
        # print(left)  # test print used to verify my understanding of logic flow
        currentValue = nums[left] + nums[right]
        # print(currentValue) # test print used to verify my understanding of logic flow
        
        if currentValue == target:
            # print("Iam here 1")  # test print used to verify my understanding of logic flow
            return True
        if currentValue > target:
            right -= 1
            # print("Iam here 2")  # test print used to verify my understanding of logic flow
        else:
            left += 1
            # print("Iam here 3")  # test print used for my understanding of logic flow
    return False

print(check_for_target(nums, 13))



"""
3. Given two sorted integer arrays, return an array that combines both of them and is also sorted. Use Two-pointer technique.


Time complexity = O(n)

- O(n) because the arrays are sorted. 
- O(n * log n) would be the result if the arrays were not sorted.

- Building the new_Array one element at a time via:
    - Comparing arr1 and arr2 values at current iteration index position.
        - Which ever is less gets added first
"""

first_array = [1, 2, 3]
second_array = [4, 5, 6]

def combine(arr1, arr2):
    new_Array = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            new_Array.append(arr1[i])
            i += 1
        else:
            new_Array.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        new_Array.append(arr1[i])
        i += 1

    while j < len(arr2):
        new_Array.append(arr2[j])
        j += 1
    
    return new_Array

print(combine(first_array, second_array))