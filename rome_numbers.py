import re
text='MCMXCIV'
def romanToInt(s):
    dict_number={
        'I':1,
        'IV':4,
        'V':5,
        'IX':9,
        'X':10,
        'XL':40,
        'L':50,
        'XC':90, 
        'C':100,
        'CD':400,
        'D':500,
        'CM':900,
        'M':1000}
   
    a=['IV','IX','XL','XC','CD','CM']
    
    pattern = '|'.join(map(re.escape, a)) + '|.'   
    result = re.findall(pattern, s)
    result = [item for item in result if item]
    
    print(pattern)
    print(result)
    
    t=0
    for i in range (0,len(result)):
        #print(t)
        t=(dict_number.get(result[i]))+t
    
    return t
            
    

print(romanToInt(text))

# example='Hello World Word!'
# r=re.sub('W.+d','Ukraine',example)
# print(r)