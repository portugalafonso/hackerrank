import numpy
#Convert string from input to int and return it as a list 
def return_list(string):
    string = string.split()
    string_list = []
    for index in string:
        string_list.append(int(index))
    return string_list

#Receive NxM (number of Lines and Coluns) from user
nm = input()
n = int(nm[:1])
m = int(nm[2:])

#List to store line and coluns from user
my_list = []
for index in range(n):
    index = input()
    #Convert and add an integer in the list
    my_list.append(return_list(index))

#Array funcions transpose and flatten
my_array = numpy.array(my_list)
print(numpy.transpose(my_array))
print(my_array.flatten())

