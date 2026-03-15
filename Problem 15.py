# Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Take the first string as a reference
        prefix = strs[0]

        for i in range(len(prefix)):
            char = prefix[i]
            # Compare this character with the same index in all other strings
            for other_str in strs[1:]:
                # If the other string is shorter or has a different character
                if i == len(other_str) or other_str[i] != char:
                    return prefix[:i]
        return prefix
