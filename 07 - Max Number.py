from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))

# The code is a list comprehension like [x for x in y]
# Here we are using underscore as a value that is not needed in the comprehension like 
# [ (function not using items) for items in list]
# So... for _ in range(k) is a for loop for the number of inputs.
# This leaves list(map(int, input().split()))[1:] which is taking the input and building a useable list.
# The map(function, iterable object) runs a function over an iterable object and in this case it is 
# turning the strings from the input into intergers after splitting the input string.
# List creates a list from the map object.
# Finally we strip the first number using the slice [1:] as it is not used 
# by the solution being the number of items in the input.
# So this line builds a list of lists with the required inputs as integers.
# You could write it like this:

# N = []
# for _ in range(k):
#     # Get input and split into list
#     l = input().split()

#     # Turn list  of strings into list of integers
#     l = list(map(int, l))

#     # Remove index [0] using a slice
#     l = l[1:]
		
#     # Build list of lists
#     N.append(l)

# N is the list of the input lists. The product(*N) creates the possible combinations as 
# tuples. Like this... (note: x, y, z are indicative here to help understand how product works
# from itertools import product

# a = [1, 2]
# b = [4, 5]
# c = ["x", "y", "z"]
# print(*product(a, b, c))
# (1, 4, 'x') (1, 4, 'y') (1, 4, 'z')
# (1, 5, 'x') (1, 5, 'y') (1, 5, 'z')
# (2, 4, 'x') (2, 4, 'y') (2, 4, 'z')
# (2, 5, 'x') (2, 5, 'y') (2, 5, 'z')

# The map function then iterates over the output of product() with the lambda function.
# lambda x: sum(i**2 for i in x)%M takes each tuple and sums the squares of each number, 
# finally performing the modulo operation. It could be written thus:
# result = 0
# for i in x:
# 	result += i**2
# result %= M
# The output of the map function provides a list of results, 
# then all we need to do is choose the maximum to solve the requirements of the challenge.