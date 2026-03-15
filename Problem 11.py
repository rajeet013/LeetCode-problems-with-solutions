# Regular Expression Matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # Initialize a table with False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: Empty string matches empty pattern
        dp[m][n] = True

        # Fill the table from bottom to top, right to left
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                first_match = i < m and (p[j] == s[i] or p[j] == '.')

                if j + 1 < n and p[j + 1] == '*':
                    # Two sub-cases for '*':
                    # 1. Ignore the x* (jump 2 steps in pattern)
                    # 2. If first char matches, move forward in string but stay in pattern
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    # Normal character match
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        
        return dp[0][0]
