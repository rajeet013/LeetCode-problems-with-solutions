# Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, return an empty list
        if not digits:
            return []

        # Mapping based on the keypad image
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"

        }
        
        res = []

        def backtrack(index, path):
            # BAse case: Current combination is complete
            if len(path) == len(digits):
                res.append("".join(path))
                return

            # Get letters for the current digit 
            possible_letters = phone_map[digits[index]]

            for letter in possible_letters:
                path.append(letter)             # 1. Choose
                backtrack(index + 1, path)      # 2. Explore next digit
                path.pop()                      # 3. Un-choose (Backtrack)

        # Start recursion from index 0 with an empty path
        backtrack(0, [])
        return res
