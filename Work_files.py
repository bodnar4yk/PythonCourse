# f=open('text.txt', 'a')
# f.write("try to write something")
# f.close()

# with open('text.txt') as f:
#     data=f.read()
#     print(data)
#     f.seek(0)


###Task1###
# with open("text.txt", 'r')as f:
#     data=f.read()
#     print(data)

###Task2###
# with open("example.txt", 'w')as f:
#     data=f.write("Hello, Python!")
#     print(data)

###Task3###
with open("example.txt", 'a') as f:
    data=f.write("Appending this line.\\n")
    print(data)