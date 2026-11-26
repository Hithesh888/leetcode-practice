class Solution(object):
    def findDuplicate(self, nums):
        n=len(nums)
        s=set()
        for num in nums:
            if num in s:
                return num
            s.add(num)
