# 3Sum Closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # Start with a sum of the first three elements
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            # Optimization: Skip duplicates for the fixed element 'i'
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == target:
                    return current_sum

                # Update closest_sum if the current gap is smaller than the old gap
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # Move pointers to try and get closer to target
                if current_sum < target:
                    left = left + 1
                else:
                    right = right - 1
            
        return closest_sum
        
