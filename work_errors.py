###Tast1###
# a=-1
# b='1'

# try:
#    c= a+b
# except TypeError:
#     print('Type error') 

###Task2###
# class managerContext ():
#     def __init__(self,file_name,method):
#         self.file_obj=open(file_name,method)
#     def __enter__(self):
#         return self.file_obj
#     def __exit__(self,type,value,traceback):
#         self.file_obj.close()

# with managerContext("test.txt", "w") as open_file:
#     open_file.write("Hola!")

###Task3###
# try:
#     int("sfjdk")
# except ValueError:
#     print("Can`t change type")

###Task4###
# class managerContext ():
#     def __init__(self,file_name,method):
#         self.file_obj=open(file_name,method)
#     def __enter__(self):
#         return self.file_obj
#     def __exit__(self,type,value,traceback):
#         self.file_obj.close()

# with managerContext("test.txt", "r") as open_file:
#     content=open_file.read()
#     print(content)

###Task5###
# dict={1:"Kyiv",2:"Lviv"}
# try:
#     #print(dict.get(2))
#     value=dict[3]
# except KeyError:
#     print("Error Key")
# finally:
#     print("Operation completed")

###Task6###
# try:
#     a=1+"wqdsad"
# except TypeError:
#     print("Error type")
# else:
#     print("No error occurred")

###Exam##
try:
    value=[1,2,3][5]
except IndexError:
    print("index out of range")