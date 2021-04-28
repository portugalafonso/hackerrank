import numpy

#Receive an input from the user
user_input = input()

#Delete spaces and create a string
user_input = (user_input.split())
string = ""
for i in user_input:
    string += i

#Create a new list with integers
input_list = []
first_item_list = False
for index in string:
    if first_item_list == False:
        input_list.append(int(index))
        first_item_list = True
    else:
        input_list.append(int(index))

#Convert the list in array
my_array = numpy.array(input_list)
my_array.shape = (3, 3)
print(my_array)