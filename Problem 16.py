# 3Sum

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort() # Sorting takes O(n log n)

        for i in range(len(nums)):
            # If the fixed number is > 0, no triplet can sum to 0 anymore
            if nums[i] > 0:
                break

            # Skip duplicate values for the fixed element
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Standard Two Pointers setup
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left = left + 1
                elif total > 0:
                    right = right - 1
                else:
                    # Found a triplet
                    res.append([nums[i], nums[left], nums[right]])

                    # Move pointers and skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1

                    left = left + 1
                    right = right - 1

        return res 
