# 4Sum

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Skipl duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Two Pointers logic
                left, right = j + 1, n - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if current_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        # Skip duploates for left and right pointers
                        while left < right and nums[left] == nums[left + 1]:
                            left = left + 1
                        while left < right and nums[right] == nums[right - 1]:
                            right = right - 1
                        left = left + 1
                        right = right - 1
                    elif current_sum < target:
                        left = left + 1
                    else:
                        right = right - 1
        return res
