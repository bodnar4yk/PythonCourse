###Task1###
# def func_dec(func):
#     def wrapper():
#         print("Start")
#         func()
#         print('End')
#     return wrapper

# @func_dec
# def add_func():
#     print("Executing function")

# add_func()

###Task2###
# import time

# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Execution time: {end_time - start_time} seconds")
#         return result
#     return wrapper

# @timing_decorator
# def my_function():
#     time.sleep(1)
#     print("Function executed")

# my_function()

###Task3###
def positive_check_decorator(func):
    def wrapper(x):
        if x > 0:
            return func(x)
        else:
            print("Argument must be a positive number")
    return wrapper

@positive_check_decorator
def print_number(x):
    print(f"The number is {x}")
print_number(5)
print_number(-3)

