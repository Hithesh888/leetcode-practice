class Solution(object):
    def maxArea(self, height):
        l=0
        r=len(height)-1
        maxWater=0
        while(l<r):
            ht=min(height[l],height[r])
            w=r-l
            currentWater=w*ht
            maxWater=max(maxWater,currentWater)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxWater