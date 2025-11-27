# # ###iterator###
# class FromOneToTwelve:
#     n=-2
#     def __iter__(self):
#         return(self)
#     def __next__(self):
#         if self.n<20:
#             self.n+=2
#             return(self.n)
#         else:
#             raise StopIteration()

# one_to_twelve=FromOneToTwelve()
# print(one_to_twelve)
# for item in one_to_twelve:
#     if item%2==0:
#         print(item)


###other_iterator####
# class EvenIterator:
#     def __init__(self):
#         self.num = -2

#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.num += 2
#         if self.num > 20:
#             raise StopIteration
#         return self.num

# even_iter = EvenIterator()
# for num in even_iter:
#     print(num)


###Generator###
# def my_func ():
#     print("test")
#     for i in range(1,11):
#         yield pow(i,2)

# for square in my_func():
#     print(square)

def simple_gen (val):
    while val>0:
        val-=1
        yield val

gen_iter=simple_gen(3)
#print(gen_iter)
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))