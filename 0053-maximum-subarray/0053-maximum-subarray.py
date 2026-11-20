
class Solution(object):
    def maxSubArray(self, nums):
        cs = 0
        ms = nums[0]
        for num in nums:
            cs += num
            ms = max(cs, ms)
            if cs < 0:
                cs = 0

        return ms
