"""
Question:
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def possible_sum(input_list, target_number):
	"""
	Check if two number can sum up to target number in a given list
	Args: input list and target number
	Returns: True if possible else false

	"""
	set1 = set()
	for number in input_list:
		if target_number - number in set1:
			return True
		else:
			set1.add(number)
	return False

a = [10, 15, 3, 7]
t = 18
print(possible_sum(a, t))


"""
Time Complexity : O(n)

traversing through each number in list
adding to set is O(1)
lookup in set is O(1)

Space Complexity: O(n)

space to store the set

"""