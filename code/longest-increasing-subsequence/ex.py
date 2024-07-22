'''

Given a given sequence, find the longest increasing subsequence (LIS) in it.

The longest increasing subsequence is a subsequence of a given sequence in which the subsequence's elements are in sorted order,
lowest to highest, and in which the subsequence is as long as possible.

The longest increasing subsequence is not necessarily unique, the solution can return any valid subsequence.

Input : [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
Output: [0, 2, 6, 9, 11, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]

'''
def longest_increasing_subsequence(sequence):
    n = len(sequence)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    length = max(dp)
    result = []
    for i in range(n - 1, -1, -1):
        if dp[i] == length:
            result.append(sequence[i])
            length -= 1
    return result[::-1]

if __name__ == '__main__':
        sequence = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        print(longest_increasing_subsequence(sequence))
