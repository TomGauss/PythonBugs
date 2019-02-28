# A string bug found in python
#The issue here is that str is a default python funciton
#if you use str in a for loop, you assign str as a string
#but you want to use it as a funciton, python does not accept it
def str_but():
    for str in range(10):
        print(str)

    print(type(str))

# str_but()

#if you run this instead above you would get an error like
#"TypeError: 'int' object is not callable"
# for str in range(10):
#     print(str)

print(type(str))
#this is because you are using str as a varialbe which over-writes the default function
#the length is incorrect, let's genereate a sequence of list and compare
LsTrainShouldChar = list(map(str, range(1, 1401)))
print(type(str))
print(len(LsTrainShouldChar))