#if you do not use copy to save a list
#then using the extend would change the original list

#implicit explnation:
#I guess this might have something to do with python language feature
#when you use list3 = list1, you might use the same memory with a different name
#this is probably why you change list3 then list1 changes as well. 
#so I guess using copy a new memory was given. 

#not copy a list would change the original list
list1 = [1, 2, 3, 4]
print("list1 is:\n", list1)

list2 = [2,3,4]

#Now try to append list2 to list1
list3 = list1
list3.extend(list2)
print("list3 is:\n", list3)
print("list1 is:\n", list1)

#initiate list1 again
list1 = [1, 2, 3, 4]

#The correct way
list3 = list1.copy()
list3.extend(list2)
print("The right way of list3 is:\n", list3)
print("The right way of list1 is:\n", list1)
