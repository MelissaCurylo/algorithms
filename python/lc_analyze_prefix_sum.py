"""
Prefix Sum Technique

- Can be used with integer arrays. 
- Prefix sums gives ability to find sum of any subarray in O(1) time. 

# Technique:
    - Create an array prefix where prefix[i] is the sum of all elements up to the index i (inclusive).
        - Example 1: Given nums = [5, 2, 1, 6, 3, 8] would have prefix = [5, 7, 8, 14, 17, 25]
        - Example 2: If needing to find the sum of the subarray from i to j (inclusive) gives this answer:
                        prefix[j] - prefix[i - 1]
                            or
                        prefix[j] - prefix[i] + nums[i]  # this deals with out of bounds case when i = 0.


# Pseudocode to build prefix sum:
    Given an integer array nums,

    prefix = [nums[0]]
    for i in [1, len(nums) - 1]:
        prefix.append(nums[i] + prefix[prefix.length - 1])


# Whenever problem involves sums of a subarray, prefix sum is the tool that costs O(n) to build BUT
    allows the future subarray queries to be at O(1) which improves the algorithm time complexity.


"""