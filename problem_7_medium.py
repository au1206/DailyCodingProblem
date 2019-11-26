"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

Leet code 91 : https://leetcode.com/problems/decode-ways/
"""


def numDecodings(data: str) -> int:
    k = len(data)

    def decode(data, k, memo):
        if k == 0:
            return 1
        s = len(data) - k
        if data[s] == '0':
            return 0
        if memo[k] != None:
            return memo[k]

        count = decode(data, k - 1, memo)

        if k >= 2 and int(data[s:s + 2]) <= 26:
            count = count + decode(data, k - 2, memo)
        memo[k] = count
        return count
    memo = [None] * (k + 1)
    return decode(data, len(data), memo)


print(numDecodings("1111"))

"""
Time Complexity without memoization: O(2^n)  worst case "111111"
Time Complexity with memoization: O(n)
Space Complexity: O(n) memoization
"""
