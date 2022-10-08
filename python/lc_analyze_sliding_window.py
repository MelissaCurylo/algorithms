"""
Sliding Window Technique

- Use for arrays or strings with contiguous ordered elements.

# Technique:
    - Sliding Windows are controlled by subarray index bounds.
    - Pointers are used but as upper and lower bounds. 
    - Best window is defined by problem and constraints. 
    - 
"""


"""
# From the given array of positive integers nums and an integer k, find the longest subarry with a sum less than or equal to k. 
    # constraint: sum(window) <= k

    # What is the time complexity?

    # Time Complexity: O(n)

        - Sliding Window algorithms run in linear time - O(n)
            - Meaning the algorithm is proportional to the size of input n. 
            - For any array that has length n then there are n subarrays of length 1. 
                -  The summation of N elements the total number of subarrays is: (n * (n+1) / 2
            - Sliding window technique has a maximum of 2n window iterations:
                - Right pointer moves n times.
                - Left pointer moves n times.
                - While loop can only iterate n times in total.
                    - Meaning the left pointer starts at 0 and only increases to never go past n.
                    - The while loop can run n times during one iteration but then won't run for the remaining iterations of loop. (amortized) 
                - Each window has O(1) time complexity.
                - Meaning after adding all the O(1) operations it ends with O(n) for tiem complexity.

"""

nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8


def longest_subarray(nums, k):
    
    left_pointer = 0
    current_sum = 0
    max_subarray = 0

    for right_pointer in range(len(nums)):

        current_sum += nums[right_pointer]

        while current_sum > k:

            current_sum -= nums[left_pointer]
            left_pointer += 1
            

        max_subarray = max(max_subarray, right_pointer - left_pointer + 1)

    return max_subarray

print(longest_subarray(nums, k))