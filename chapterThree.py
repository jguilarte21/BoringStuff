### Functions
### Author: Justin Guilarte 

"""
- Function - Group of code that performs a certain operation 
Ex.
def functionName(parameter):
    FUNCTION 

- NONE Value
    - Basically the same thing as null 

Keyword Arguments 
- Most arguments are identified by their position in the function call 
Ex.     random.randint(1, 10) <-- is different from --> random.randint(10, 1)

- Keyword Arguments - idetified by the keyword put before them in the function call 
Ex.     print('Hello')


Global Scope
- If you need to make a variable of global value, use the keyword
Ex.     global eggs

Exception Handling
- You can use try catch blocks to handle exceptions 


"""


### The Collatz Sequence

def collatz(number):
    num = number
    print("The number that you input was", num)
    while num > 1:
        # If the number is odd 
        if (num % 2 == 1):
            num = 3 * num + 1
            print("Your number is odd, new number is", num)
        elif (num % 2 == 0):
            num = num // 2
            print("Your number is even, new number is", num)

    print("Final number", num)
        

print("Input a number greater than 1")
collatz(int(input()))



