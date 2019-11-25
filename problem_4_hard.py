"""This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input[3, 4, -1, 1] should give 2. The input[1, 2, 0] should give 3.

You can modify the input array in-place.

 Leet 41 https://leetcode.com/problems/first-missing-positive/
"""

"""space complexity : O(n)
time complexity : O(n)
def firstMissingPositive(data):
    m = max(data)
    l = [0] * (m + 2)
    for elem in data:
        if elem >= 0:
            l[elem] = 1
    for el in range(1, len(l)):
        if l[el] == 0:
            return el"""


# space complexity : O(1)
# time complexity: O(n)
def firstMissingPositive(data):
    if len(data) == 0:
        return None
    for elem in range(1, len(data) + 2):
        if elem not in data:
            return elem



# TEST
data1 = [3, 4, -1, 1]
data2 = [1, 2, 0]
data3 = [7, 8, 9, 11, 12]
print(firstMissingPositive(data2))
