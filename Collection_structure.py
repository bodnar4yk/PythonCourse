#####list######
###Task1###
# planets=['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# planets.append('Pluto')
# print(planets)

###Task2###
# planets=['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# planets.remove('Mars')
# print(planets)

###Task3##
# numbers=[9, 21, 12, 1, 3, 15, 18]

# numbers.sort(reverse=True) #reverse=True desc
# print(numbers)

###Task4###
# list1 = ["Tom", "Bob", "Alice"]
# list2 = ["Sam", "Tim", "Bill"]

# print(list1+list2)

##################################
###Tuple###
###Task1##
# planets =("Mercury", "Venus", "Earth", "Mars")
# print(planets)

###Task2##
# planets =("Mercury", "Venus", "Earth", "Mars")
# list=list(planets)
# print(planets)

##################################
###Dictionary###
###Task1###
# capitals={'Ukraine':'Kyiv', 'France':'Paris', 'Germany':'Berlin'}
# print(capitals)

###Task2###
# capitals={'Ukraine':'Kyiv', 'France':'Paris', 'Germany':'Berlin'}
# capitals['Italy']='Rome'
# print(capitals)

###Task3###
# capitals={'Ukraine':'Kyiv', 'France':'Paris', 'Germany':'Berlin','Italy':'Paris'}
# del capitals['Italy']
# #capitals.pop("France")
# print(capitals)

###Task3###
# capitals={'Ukraine':'Kyiv', 'France':'Paris', 'Germany':'Berlin','Italy':'Paris'}
# # a=capitals.get('Germany')
# # print(a)

# capitals = {"Ukraine": "Kyiv", "France": "Paris", "Germany": "Berlin"}
# if "Germany" in capitals:
#     print("Germany is in the dictionary")
# else:
#     print("Germany is not in the dictionary")

##################################
###Set###
###Task1###
# fruits={"apple", "banana","cherry"}
# print(fruits)

###Task2###
# fruits={"apple", "banana","cherry"}
# fruits.add("orange")
# print(fruits)

###Task3###
# fruits={"apple", "banana","cherry"}
# fruits.remove("banana")
# print(fruits)

###Task4###
# set1={1, 2, 3}
# set2={3, 4, 5}

#print(set1|set2)
# combine_set=set1.union(set2)
# print(combine_set)

##########
###Exam###
# set1=[1, 2, 3]
# print(set1.index(2))

# weekdays=["m","t","w",'tr',"f",'sat','sunday']
# print(weekdays[2],weekdays[-1])

# weekdays=("m","t","w",'tr',"f",'sat','sunday')
# print(weekdays[2],weekdays[-1])

# weekdays=("m","t","w",'tr',"f",'sat','sunday')
# print(min(weekdays),max(weekdays))

capitals={'Ukraine':'Kyiv', 'France':'Paris', 'Germany':'Berlin'}
print(capitals.keys())
