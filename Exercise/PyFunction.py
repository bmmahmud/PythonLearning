####  Function
# def fun():
#     print('Function Print')


# fun()

## Argument
# def names(fname,lname): # parameter as input
#     print(f"First Name: {fname}")
#     print(f"Last Name: {lname}")

# names("Ashik","Mahmud") # Value as Argument

## Type of Function
# 1- Perform a task 2- Return a value

# def increment(num,by):
#     return num+by

# print("Result: ",increment(2,1))  
   
# def multiply(*num):
#     total =1
#     for n in num:
#         total *= n
#     return total

# print('Multiplication : ',multiply(1,2,3,4))

def fizz_buzz(input):
    if input % 3 == 0:
        return "Fizz"
    else:
        return "Buzz"


print(fizz_buzz(15))