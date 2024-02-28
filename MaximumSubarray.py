class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm
        max_ending_here = 0
        max_so_far = -math.inf - 1

        for num in nums:
            max_ending_here += num
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        
        return max_so_far
