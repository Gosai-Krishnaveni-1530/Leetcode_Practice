class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        pal = [[False] * n for _ in range(n)]

        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                if s[l] == s[r] and (r - l <= 1 or pal[l + 1][r - 1]):
                    pal[l][r] = True

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
 
            dp[i] = dp[i - 1]

            if i >= k:
                l = i - k
                if pal[l][i - 1]:
                    dp[i] = max(dp[i], dp[l] + 1)

            if i >= k + 1:
                l = i - k - 1
                if pal[l][i - 1]:
                    dp[i] = max(dp[i], dp[l] + 1)

        return dp[n]