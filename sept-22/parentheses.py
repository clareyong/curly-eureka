class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(i, n + 1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if s[i-1] == '(' and s[j-1] == ')':
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 2)
        return dp[n][n]