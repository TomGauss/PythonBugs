#if you do not use copy to save a list
#then using the extend would change the original list

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
