class Solution:
    def numDistinct(self, s, t):
        n = len(t)
        dp = [0] * (n + 1)
        dp[0] = 1

        for ch in s:
            for j in range(n, 0, -1):
                if ch == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]