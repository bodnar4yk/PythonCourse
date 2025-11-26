###Task1###
# def test (a,b):
#     return(a+b)

# test(2,5)

##Task2###
# def greet (name):
#     print(f"Hello, {name}!")

# greet('Name')

###Task3###
# data=[1,2,3,4]
# a=lambda x : x**2
# result=list(map(a,data)) 
# print(result)

###Task4### return func with arg
# def apply_function (func,x):
#     return func(x)


###try usedURL###
# import requests
# def sourcetemplete(url):
#     def load(**kwargs):
#         return requests.get(url.format_map(kwargs))
#     return load
# load = sourcetemplete("https://api.github.com/repositories?since={since}")
# load(since=200).json()
# print(2)


###test9###
# def mult(a,b=2):
#     return a*b
# print(mult(3))

###test10###
# def greet (name="Guest"):
#     return f"Hello, {name}!"
# print(greet())

###test11###
def outter_function(x):
    def inner(y):
        return x+y
    return inner

add_five=outter_function(5)
print(add_five(10))