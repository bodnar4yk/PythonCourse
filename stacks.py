s="()))"

def stack(s):
    Steck=[]
    dict_element={'(':')', '[':']','{':'}'}
    ls=list(s)
    if ls[0] in (')','}',']') or len(ls)%2!=0:
        return False      
    else:
        for i in range(0,len(ls)):
            element=ls[i]
            if element in ('(', '{','['):
                Steck.append(element)
            elif element in (')','}',']') and len(Steck)>0 and element==dict_element.get(Steck[-1]):
                Steck.pop()
            else:
                return False     
        if len(Steck)>0:
            return False
        else:
            return True               

print(stack(s))
    
