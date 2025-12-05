###Task1###
# import threading

# def func(start,end):
#     for i in range(start,end+1):
#         print(f"list:{i}") 

# t1=threading.Thread(target=func,args=(1,5))
# t2=threading.Thread(target=func,args=(6,10))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

###Task2###
# import math
# import multiprocessing

# def factorial(n):
#     result=math.factorial(n)
#     print(result)


# process1=multiprocessing.Process(target=factorial,args=(5,))
# process2=multiprocessing.Process(target=factorial,args=(10,))

# process1.start()
# process2.start()

# process1.join()
# process2.join()

###Task3###
# import asyncio
# async def func(n,delay):
#     await asyncio.sleep(delay)
#     print(f"task{n}, wait{delay}")



# async def main():
#     task1=asyncio.create_task(func("a",3))
#     task2=asyncio.create_task(func('b',4))
#     task3=asyncio.create_task(func("c",5))

#     await task1
#     await task2
#     await task3

# asyncio.run(main())

###Task4###
import time
import math
import threading 

def factorial(n):
    result=math.factorial(n*n)
    print(result)
start_time = time.time()

t1=threading.Thread(target=factorial,args=(100))
t2=threading.Thread(target=factorial,args=(200))
t1.start
t1.join
t2.start
t2.join

end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")