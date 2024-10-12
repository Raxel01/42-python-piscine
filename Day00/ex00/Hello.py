ft_list = ["Hello", "tata!"]
# This will be World!
ft_tuple = ("Hello", "toto!")
# country of my campus Moroco
ft_set = {"Hello", "tutu!"}
# city Khouribga
ft_dict = {"Hello" : "titi!"}
# 1337-khouribga

# List
# acces specific range [start:end] list[end] is excluded
# get last element by using [-1]
# insert methode insert an elemnt at specific position
# add items by  append at the End ot insert on specific position
ft_list[-1] ="World!"
# add List to a list using extend list1.extend(list2)
# remove remove the Specifyed items using list.remove(item)
# remove using index pop(index) del items so list[index]

# Tuples
tupleToList = list(ft_tuple)
tupleToList[-1] = 'Morocco'
ft_tuple = tuple(tupleToList)
# ordered and unchangeable
# cant add or remove items after tuple is created 
# Allow Duplicates
# accessing elements is like list ,
# 

#***-- SET **--
# set is unordered, unchangeable*, and unindexed
# unchangable like tuple
# add() to add elemnts to set
# update add a set to a set ! (set1 | set2)
# use remove , discard
# setToList = list(ft_set)
# print('*******')
# print(setToList)
# print('*******')
newft_set = {x if x != "tutu!" else "Khouribga"  for x in ft_set}
ft_set = newft_set

#Dictionnary*********/
# up 3.7 dict ar ordred
# acces elemnts by ['key'] , dict.keys(), dict.values(), dict.get()
# change elemnts by ['key'] = newValue 
# update ({Existedkey : Newvalue})
# add elemnts by update({key, value})
# remove elemnts : {
    # pop('key');
    # popitem() remove last inserted index in 3.7 up
    # 
# Empty the Dictionnary 
    # dict.clear()
    # del list will remove it no longer exist !
# }
ft_dict['Hello'] = '1337-khouribga'
# 1337-khouribga
# //*****************/

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
