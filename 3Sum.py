class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        # Picking up one number first every time from smallest to largest
        for i in range(len(nums)):
            if i > 0:
                # Skipping the duplicate ones
                if nums[i] == nums[i - 1]:
                    continue
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]: 
                        right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    right -= 1

        return result
