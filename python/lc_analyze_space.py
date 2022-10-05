"""
1. 

Given an array "arr" with length n,

for (int num: arr) {
    print(num)
}

Space complexity = O(1)

- Only space allocated is for the integer variable num.
- Integer variable num is constant relative to n. 

"""


"""
2.

Given an array "arr" with length n,

Array doubledNums = int[]

for (int num: arr) {
    doubledNums.add(num * 2)
}

Space complexity = O(n)

- Array doubledNums is storing n amount of integers.
- Storing is happening at the end of the algorithm and allocating the integer to the array.
    - doubledNums.add(num * 2)

"""


"""
3.

Given an array "arr" with length n,

Array nums = int[]
int oneHundredth = n / 100

for (int i = 0; i < oneHundredth; i++) {
    nums.add(arr[i])
}

Space complexity = O(n)

- Array nums stores the first 1% of numbers in arr.
- 1% comes from the int oneHundredth where we take any n value from 1 to 100 and divide it by 100. (1/100 = 0.001 or 1%)
- The space complexity would be O(n/100) = O(n).

"""

"""
4. 

Given an array "arr" with length n,
Given an array "arr2" with length m,

Array grid = int[n][m]

for (int i = 0; i < arr.length; i++){
    for (int j = 0; j < arr2.length; j++){
        grid[i][j] = arr[i] * arr[j]
    }
}

Space complexity = O(n * m)

- This algorithm is creating a grid where n * m will be the dimensions through each iteration via variable i and j. 

"""