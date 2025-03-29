# 1
# Write a function fibonacci(n) that calculates the nth Fibonacci number without using recursion. Use an iterative approach to compute the result.

# def fibonacci(n):
#     if n <= 0:
#         return "Input must be a positive integer"
#     elif n == 1:
#         return 0  
#     elif n == 2:
#         return 1  
    
#     a, b = 0, 1  
#     for _ in range(2, n):
#         a, b = b, a + b  
#     return b

# print(fibonacci(6)) 




# 2
# Write a function factorial(n) that calculates the factorial of a given number using an iterative approach. 

# def factorial(n):
#     if n < 0:
#         return "Input must be a non-negative integer"
    
#     result = 1  
#     for i in range(1, n + 1):
#         result *= i  
    
#     return result


# print(factorial(5))




# 3
# Write a function is_prime(n) that checks if a number is a prime number using a loop. The function should return True if the number is prime and False otherwise.


# def is_prime(n):
#     if n <= 1:
#         return False  
#     for i in range(2, int(n ** 0.5) + 1):  
#         if n % i == 0:  
#             return False
    
#     return True 

# print(is_prime(11))  
# print(is_prime(15))



# 4
# Write a function reverse_string(s) that reverses a string without using slicing or built-in functions like reversed(). Use a loop to construct the reversed string.

#  def reverse_string(s):
#     reversed_s = ""
#     for char in s:
#         reversed_s = char + reversed_s  
#     return reversed_s

# print(reverse_string("hello"))





# 5
# Իրականացնել ֆունկցիա, որն ընդունում է թիվ և վերադարձնում նրա թվանշանների գումարը: 

# def sum_of_digits(number):
    
#     number = abs(number)
    
#     total = 0  
#     while number > 0:
#         total += number % 10  
#         number //= 10  
    
#     return total


# print(sum_of_digits(123))  
# print(sum_of_digits(-456)) 



# 6
# Իրականացնել int տիպի արժեք վերադարձնող ֆունկցիա, որը վերադարձնում է՝ 1,
#  եթե ֆունկցային փոխանցված ամբողջ թիվը կարող է արտահայտվել երկու պարզ թվերի գումարով, հակառակ դեպքում ֆունկցիան կվերադարձնի՝ 0:

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def can_be_expressed_as_sum_of_two_primes(num):
#     if num < 4:  
#         return 0
    
    
#     for i in range(2, num):
#         if is_prime(i) and is_prime(num - i):
#             return 1  
#     return 0  


# print(can_be_expressed_as_sum_of_two_primes(10))  
# print(can_be_expressed_as_sum_of_two_primes(11))





# 7
# Իրականացնել ֆունկցիա, որը ունի հետևյալ նախատիպը (prototype)  def power (num: int, exp:int): Ֆունկցիան վերադարձնում է num ամբողջ թվի exp աստիճանի արժեքը։

# def power(num: int, exp: int) -> int:
#     result = 1
#     for _ in range(abs(exp)):
#         result *= num  
    
    
#     if exp < 0:
#         return 1 / result
#     return result


# print(power(2, 3))  
# print(power(5, -2))  
# print(power(3, 0))  




# 8
# Մուտքագրել թիվ, տպել թվի թվանշանները առանձին առանձին էկրանին։ Օրինակ՝ մուտքագրված 5479 թվի համար տպել ‘5’, ‘4’, ‘7’, ‘9’։

# def print_digits(number):
    
#     for digit in str(abs(number)):  
#         print(digit)


# number = int(input("Մուտքագրեք թիվը: "))  
# print_digits(number)