'''

Given an unlimited supply of coins of given denominations, find the minimum number of coins required to get the desired change.

Input: S = [1, 3, 5, 7], target = 15
Output: 3
Explanation: The minimum number of coins required is 3 (7 + 7 + 1) or (5 + 5 + 5) or (3 + 5 + 7)

Input: S = [1, 3, 5, 7], target = 18
Output: 4
Explanation: The minimum number of coins required is 4 (7 + 7 + 3 + 1) or (5 + 5 + 5 + 3) or (7 + 5 + 5 + 1)

If desired change is not possible, the solution should return -1.

Input: S = [2, 4, 6, 8], target = 15
Output: -1

'''

def mainCoins(s, target, dp):
    if target < 0: # base case
        return -1
    if dp[target] != -1: # if the value is already calculated (dp inicdetes dynamic programming)
        return dp[target]
    result = float('inf') # set the result to infinity
    for i in range(len(s)):
        temp = mainCoins(s, target - s[i], dp) # recursive call
        if temp != -1: # if the value is not -1
            result = min(result, temp + 1) # get the minimum value
    dp[target] = result if result != float('inf') else -1 #if the result is not infinity, set the value to result, else set it to -1
    return dp[target] # return the value


if __name__ == "__main__":
    s = [2, 4, 6, 8]
    target = 15
    dp = [-1] * (target + 1)
    dp[0] = 0
    res = mainCoins(s, target, dp)
    print(res)
