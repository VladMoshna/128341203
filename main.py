# def get_discounted_prices(prices: list):
#     discounted_prices = []

#     for price in prices:
#         if price > 100:
#             new_price = price * 0.8
#             discounted_prices.append(new_price)

#     return discounted_prices

# original_prices = [50, 120, 80, 200, 300]
# result = get_discounted_prices(original_prices)
# print(result)
# import sys
# sys.setrecursionlimit(10000)
# def recursion():
#     print("recursion")
#     recursion()

# recursion()

# def func_a():
#     print("A call B")
#     func_b()

# def func_b():
#     print("B call A")
#     func_a()


# def factorial_loop(num):
#     result = 1
#     for i in range(1, num + 1):
#         result *= i
#     return result

# def factorial_recursion(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial_recursion(num - 1)

# print(factorial_loop(5))
# print(factorial_recursion(5))

# def some_func():
#     print("Hello")

# func_var = some_func

# print(type(func_var))
# func_var()

# # callback function

# def some_func_with_callback(callback):
#     print("funcrion that cals another function")
#     callback()

# def print_greet():
#     print("Greeting!")

# some_func_with_callback(some_func)
# some_func_with_callback(print_greet)

# summ = lambda a, b: a + b

# print(summ(10, 12))
    
# operations = {
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a - b,
#     "*": lambda a, b: a * b,
# }

# num1 = float(input("Введіть перше число: "))
# num2 = float(input("Введіть друге число: "))
# action = input("Enter sign(+, -, *): ")

# if action in operations:
#     print(operations[action](num1, num2))
# else:
#     print("incorrect sign!")


# tax_rate = 0.2

# def calc_tax_impure(amount):
#     return amount * tax_rate


# def calc_tax_pure(amount, tax_rate):
#     return amount * tax_rate

# print(calc_tax_pure(10, 0.3))

# my_cart = ["apple", "banana"]

# def add_product_impure(cart, product):
#     cart.append(product)
#     return cart

# add_product_impure(my_cart, "orange")
# print(my_cart)

# def add_product_pure(cart: list, product: str) -> list:
#     new_cart = cart.copy
#     new_cart.append(product)
#     return new_cart

# new_cart = add_product_pure(my_cart, "orange")
# print(new_cart)
# print(my_cart)

# def create_multiplier(factor):
#     def multiplier(number):
#         return number * factor
#     return multiplier

# double = create_multiplier(2)
# triple = create_multiplier(3)

# print(double(3))
# print(triple(9))

# my_list = [15, 8, 42, 4, 16, 23]

# even = []

# for num in my_list:   # імперативний підхід
#     if num % 2 == 0:
#         even.append(num)

# even_numbers = list(filter(lambda a: a % 2 == 0, my_list))   # декларативний

# print(even_numbers)

def changecase(func):
    def inner():
        return func().upper()
    return inner

@changecase
def my_function():
    return "Hello, Sally!"

@changecase
def goodboy():
    return "goodby, Saly!"

print(my_function())
print(goodboy())