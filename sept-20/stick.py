def stick(n, length, profit):

    dp = [0] * (n + 1)
    dp[1] = profit[0]

    for i in range(1,n):
        for j in range(i):
            dp[i+1] = max(dp[i-j] + profit[j], profit[i], dp[i+1])

    return dp[n]

    """
    Questions:
    - what if n is greater than the number of lengths? e.g. n = 10

    """

def stick(n, length, profit):

    dp = [0] * (n + 1)
    dp[1] = profit[0]

    for i in range(1,n):
        for j in range(i):
            if i < len(profit):
                dp[i+1] = max(dp[i-j] + profit[j], profit[i], dp[i+1])
            else:
                print(i, j)
                dp[i+1] = max(dp[i+1], dp[j] + dp[i-j+1])
    print(dp)

    return dp[n]

length = [1,2,3,4,5]
profit = [2,5,8,1,3]
n = 6
print(stick(n, length, profit))
