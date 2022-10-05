"""
Recursion vs Iterative:

- Recursion focuses on function calls to simulate repeated code.
- Iterative focuses on for loops and while loops to simualte repeated code. 

"""


"""
1.
Iteravtive algorithm 

for (int i = 1; i <= 10; i++) {
    print(i)
}

"""


"""
2.
Recursive algorithm

- Every call to fn will print the variabl i value.
- Aftery printing the variable i value, the function fn is called again.
    - This time adding the variable i value to 1 so incrementing i to print the next value.
- There isn't a base case so this would never reach the return statement and stack overflow to infinity and likely crash in time. 

"""
# def fn(i):
#     print(i)
#     fn(i + 1)
#     return
# fn(1)


"""
3. 
Adding a base case

"""
def fn(i):
    if i > 10:
        return

    print(i)
    fn(i + 1)
    return
fn(1)




"""
4. 
Understanding order of recursive cascades

- fn(1) is calling the fn function.
- First the fn(1) makes the calls and prints in this order through each call:
    - fn(1) call with output = 1
    - fn(2) call with output = 2
    - fn(3) call with outpu = 3
- Second the recusive function moves "back up" via fn(4) because the base case is triggered and nothing gets printed. 
- Third, due to hitting the base we are sent back into the function where i = 3.
    - i = 4 hits base case and sends recusive function into "reverse" to work backt o fn(1). 
    - i = 3 because fn(i + 1) is fn(2 + 1).
    - i = 2 because fn(i + 1)  is fn(1 + 1).
    - Repeats until fn(1)

- In recursion the function calls until it can't call itself anymore and left with many small pieces or problems to solve. After hitting the base case, recursion works in reverse 
    to arrive back at the original call which was fn(1).

"""
def fn(i):
    if i > 3:
        return 

    print(i)
    fn(i + 1)
    print(f"End of call where i = {i}")
    return
fn(1)



"""
5. 

Recurrence relation via Fibonacci Numbers

F(3) = 2

Flow of calling F(3):
    - Broken down into subproblems of F(2) and F(1) then combining recurrence relation and base case to solve problem.
    - First, conditional checks if F(2) is less than or equal to 1 and it's not.
    - Second, oneBack take passed in argument of 2: 2 - 1 = 1
    - Third, twoBack gets the value passed of 2: 2 - 2 = 0
    - Fourth, adding oneBack + twoBack = 1
    - Recursion function repeats then hits base case and returns 2. 

"""

def F(n): 
    if n <= 1:
        return n
        

    oneBack = F(n - 1)
    # print(f"oneBack = {oneBack}") # using print to test what is the actual value
    twoBack = F(n - 2)
    # print(f"twoBack = {twoBack}") # using print to test what is the actual value

    return oneBack + twoBack

print(F(3))