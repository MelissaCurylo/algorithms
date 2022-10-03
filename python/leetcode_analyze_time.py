"""
1. 

Given an arry "arr" with length n, 

for (int num: arr){
    print(num)
}

Time complexity = O(n)

- each for loop iteration performs a print = O(1).
- each for loop iterates n times input = O(n).
- O(n) where n tends towards infinity or to the limits of inputs but drop the constants. 
- Time Complexity = () 1 * n) = O(n).
"""


"""
2. 

Given the array "arr" with length n,

for (int num: arr) {
    for (int i = 0; i < 500,000; i++){
        print(num)
    }
}

Time complexity = O(n)

- Two for loops that are nested.
- Inner for loop iteration has a print function = O(1) = constant time.
- Outer for loop iterates n times which is 500,000 times = O(500,000) = O(n).
- This algorithm is much slower than number 1 due to the input size the algorithm needs to iterate and print. 

"""


"""
3.

Given an array "arr" with length n,

for (int num: arr) {
    for (int num2: arr) {
        print (num * num2 )
    }
}

Time complexity = O(n^2)

- Each inner for loop has a print function with multiplication = print = O(1) and multiplication = O(1) // Both == O(1).
- Inner for loop iterates n times = O(n).
- Outer for loop iterates n times = O(n).
- Nested behavior of for we multiply the variables: O(n * n) = O(n^2).

"""



"""
4.

Given an array "arr" with length n,
Given an array "arr2" with length m,

for (int num: arr) {
    print(num)
}
for (int num: arr) {
    print(num)
}
for (int num: arr2) {
    print(num)
}

Time complexity = O(n + m)

- First two for loops have iteration and print = O(1)
    - each for loop iteration performs a print = O(1).  
    - each for loop iterates n times input = O(n).
- Last for loop iterates and performs print but gets a different variable as different array = O(m)
- Time complexity = O(2n + m) == O(n + m)

"""



"""
5.

Given an array "arr" with length n,

for( int i = 0; i < arr.length; i++ ) {
    for ( int j = i; j < arr.length; j++ ) {
        print( arr[i] + arr[j] )
    }
}

Time complexity = O(n^2)

- Inner for loop is dependent on the outer for loop current iteration. 
    - Which means if the outer for loop has finished iterating the inner for loop would no longer iterate.
- Inner Loop behavior:
    - First run the inner loop iteration runs n times.
    - Second run the inner loop iteration runs n times - 1. (n - 1)
    - Third run the inner loop iteratio runs n times - 2. (n -2)
    - Continues pattern until hitting bounds.
    - This pattern creates a partial sum to the total time complexity.
        - Meaning the total inner for loop iterations =  1 + 2  + ... + n
        - Mathematically looks like: 
                  n * (n+1)             n^2 + n
                -------------   =    -------------   =  O(n^2)
                    2                       2
        - The addition terms in the numerator and the divided constant int he denominator are ignored.
        - Dropping constants because we do not need the absolute magnitudes of an algorithm but more so the long term growth rate of the functionality. 
"""