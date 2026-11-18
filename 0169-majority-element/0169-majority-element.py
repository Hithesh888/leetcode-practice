class Solution(object):
    def majorityElement(self, nums):
        count=0
        candidate=0
        for num in nums:
            if count==0:
                candidate=num
            
            if candidate==num:
                count=count+1
            else:
                count=count-1
        return candidate
        
        