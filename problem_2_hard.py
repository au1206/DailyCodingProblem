"""
Question:
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array 
except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def new_prod_array(input_array):
	"""
	creates a new array with product of all element but 1
	Args: input array
	Returns: new prod array
	"""

	new_array = []
	prod = 1
	for elem in input_array:
		prod = prod*elem
	for elem in input_array:
		new_array.append(prod//elem)

	return new_array


a = [1, 2, 3, 4, 5]
assert (new_prod_array(a) == [120, 60, 40, 30, 24]),"Failed"

print(new_prod_array(a))

"""
TIME COMPLEXITY: O(n)
2 un cascaded for loops

SPACE COMPLEXITY : O(n)
storing the entire new array and prod
"""


# WITHOUT DIVISION
# can also be done with multiple cascaded for loops in longer time

import math
def new_prod_array(input_array):
	"""
	creates a new array with product of all element but 1
	Args: input array
	Returns: new prod array
	"""

	new_array = []
	sum1 = 0
	for elem in input_array:
		sum1 = sum1 + math.log10(elem)
	for elem in input_array:
		new_array.append(round(pow(10,sum1-math.log10(elem))))

	return new_array


a = [1, 2, 3, 4, 5]
print(new_prod_array(a))
assert (new_prod_array(a) == [120, 60, 40, 30, 24]),"Failed"


"""
TIME COMPLEXITY: O(n)
2 un cascaded for loops

SPACE COMPLEXITY : O(n)
storing the entire new array and prod
"""
