class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                p = j+1
                q = n-1

                while p < q:
                    total = nums[i] + nums[j] + nums[p] + nums[q]

                    if total > target:
                        q -= 1

                    elif total < target:
                        p += 1

                    else:
                        res.append([nums[i], nums[j], nums[p], nums[q]])

                        p += 1
                        q -= 1

                        while p < q and nums[p] == nums[p-1]:
                            p += 1

                    
        return res
