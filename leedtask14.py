import re
import collections
strs=["flower","flow","flight",'flow','carrr','flight']#["ccir","ccar"]#,'adsfd']

def check(strs):
    strs.sort(key=len)
    letter=list(strs[0])
    if len(strs)==1:
        return strs[0]
    else:
        for n in range(1,len(strs)):
            for i in range(0,len(letter)):
                if letter[i] == list(strs[n])[i]:
                    pass
                else:
                    print(i)
                    letter=letter[:i]
                    break
        
        return ''.join(letter)  
                
#print(check(strs))

def longestCommonPrefix(srts):
    if not strs:
        return ""
    s1=min(strs)
    s2=max(strs)

    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            return s1[:i]
    return s1

print(longestCommonPrefix(strs))