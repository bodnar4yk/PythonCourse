number=126621
# def polindrome(number):
#     x=list(str(number))
#     leng=int(len(str(number)))
#     print(leng)
#     k=0

#     for i in range(0,leng//2):
#         print(x[i],x[-i-1])
#         if  x[i]==x[-i-1]:
#             print(i,x[i], x[-i-1],leng//2)
#             k+=1
#             print(k)
#     if (k==leng//2 and k!=0) or leng==1:
#         print(leng//2)
#         print(x)
#         print('this is polindrome')
#         return True          
#     else:
#         print('this is NOT polindrome')
#         return False

def polindrome(x):
    print(str(x))
    return str(x)==str(x)[::-1]
        
    
#print(int(len(str(number))))
print(polindrome(number))
