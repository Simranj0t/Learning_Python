# Function to Greet someone 
# def greet():
#     print("Hello")
# greet()

# # Greet with Taking the name as input 
# def greet(name):
#     return(f"Hello, {name}")
# greeting = greet("Preetam")
# print(greeting)

# #function to Add two numbers 

# def add(a,b):
#     return sum([a,b])
# print(add(3,4))

# def add(a,b):
#     return a + b
# print(add(3,4))

# To find the Square of a term
# def square(n):
#     return n * n
# print(square(5))

# def square(n):
#     return n*n
# print(square(3))

# def power(base, exp=2):
#     return base ** exp
# print(power(5))

# def income(name,age):
#     print(f"My name is {name},and my age is {age}")
# income(age=20,name="Preetam")

# def introduce(name,age):
#     print(f"Hello Brother my name is {name} and my age is {age}")
# introduce("simran",25)

# x = 10

# def modify():
#     x = 5
#     print(x)

# modify()
# print(x)

# Write a function is_even(n) that returns True if a number is even, otherwise False.
# def is_even(n):
#     if n%2 == 0:
#         print(f"Number {n} is Even")
#     else:
#         print(f"Number {n} is odd")
# is_even(25)

#Write a function max_of_three(a, b, c) that returns the largest of three numbers.

# def max_of_three(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c

# print(max_of_three(a=1, b=2, c=3))

# add two numbers
# def add_num(a,b):
#     return a+b
# print(add_num(5,6))

# def sq(n,exp=2):
#     return n ** exp
# print(sq(4))

# def fact(n):
#     f = 1 
#     for i in range(1,n+1):
#         f = f*i
#     return f
# print(fact(5))

# def rev(a):
#     res =""
#     for i in a:
#         res = i + res
#     return res
# print(rev("Simran"))

# def pal(a):
#     b = a
#     rev = 0
#     while a > 0:
#         rem = a % 10        # get last digit
#         rev = rev * 10 + rem
#         a = a // 10 
#     if(rev == b): 
#         return "Palindrome"
#     else:
#         return "Not a Palindrome"    
# print(pal(121))


# is prime
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1): # it will check till the root of that number +1 example 36 root =6 +1 means it will check from 2 to 6 
#         if n % i == 0:
#             return False
#     return True

# # Example usage
# num = int(input("Enter a number: "))

# if is_prime(num):
#     print(f"{num} is a Prime Number")
# else:
#     print(f"{num} is NOT a Prime Number")

# Function to Show Default arguments are evaluated once, not every call
# def add_item(item, my_list=[]):
#     my_list.append(item)
#     return my_list

# print(add_item(1))  # [1]
# print(add_item(2))  # [1, 2]  <-- unexpected!
# print(add_item(3))  # [1, 2, 3]

# Correct one -
# def add_item(item, my_list=None):
#     if my_list is None:
#         my_list = []
#     my_list.append(item)
#     return my_list

# print(add_item(1))  # [1]
# print(add_item(2))  # [2]
# print(add_item(3))  # [3]

# Working on a Counter be like - 

# def counter(count=[0]):
#     count[0] += 1
#     return count[0]

# print(counter())  # 1
# print(counter())  # 2
# print(counter())  # 3

# A simple Shopping Problem -
# def calculate_total(price, tax=0.18, discount=0):
#     # Edge cases
#     if price < 0:
#         raise ValueError("Price cannot be negative")
    
#     if discount > price:
#         raise ValueError("Discount cannot exceed price")
    
#     # Apply discount first
#     discounted_price = price - discount
    
#     # Apply tax
#     final_amount = discounted_price * (1 + tax)
    
#     return final_amount
