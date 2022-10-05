"""
Leetcode # 11 - Container With Most Water (Medium)

Link -> https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    1. Find two lines that together with the x-axis form a container, such that the container contains the most water.

    2. Return the maximum amount of water a container can store.

    3. Notice that you may not slant the container.


Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:
    Input: height = [1,1]
    Output: 1

Constraints:
    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104

"""

height = [1,8,6,2,5,4,8,3,7]

# class Solution:
# def maxArea(self, height: list[int]) -> int:

def maxArea(height):

    i = 0
    j = len(height) - 1
    largest_container = 0

    
    while i != j:
        
        current_capacity = min(height[i], height[j]) * (j - i)

        if current_capacity > largest_container:
            largest_container = current_capacity

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return largest_container

print(maxArea(height))




"""
    Two-pointer technique:
        1. Create two pointers:
            1a. pointer one at index zero.
            1b. pointer two at index end of array.
        2. Store the largest value to keep track of largest baseline.
        3. Create loop to check each index
            3a. Loop ends when pointers are equal to each other. 
            3b. Iterate from the shorter point, so compare the heights and iterate from the smaller one.
        4. Store current iteration value which is the the container size.
            4a. Container size is defined by the distance between two indices (x2-x1) and then multiplied by shorter vertical bar (y value).
                - (x2-x1) * (minimum of (y))
        5. Compare largest container variable to current variable then update larger value to largest container.
        6. Update index iteration by the comparing whichever one is shorter.


"""