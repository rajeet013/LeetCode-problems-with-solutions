# Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        n = len(s)

        for i in range(n):
            current_val = roman_map[s[i]]

            # Check if there is a next character and if it's larger
            if i + 1 < n and current_val < roman_map[s[i + 1]]:
                # Subtractive case
                total = total - current_val
            else:
                # Normal case
                total = total + current_val
        
        return total
