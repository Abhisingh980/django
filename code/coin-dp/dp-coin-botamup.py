import sys
def findMinCoins(S, target):
    dp = [sys.maxsize] * (target + 1)
    dp[0] = 0
    for i in range(target+1):
        for coin in S:
            if i - coin >= 0:
                dp[i] = min(dp[i],dp[i-coin]+1)
    return dp[target]

if __name__ == '__main__':
    S = [1,3,5,7]
    target = 15
    coins = findMinCoins(S, target)
    if coins != sys.maxsize:
        print('The minimum number of coins required to get the desired change is', coins)
    else:
        print(-1)
