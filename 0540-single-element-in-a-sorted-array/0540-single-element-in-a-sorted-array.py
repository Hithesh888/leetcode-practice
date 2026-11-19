
class Solution(object):
    def singleNonDuplicate(self, nums):

        n = len(nums)

        if n == 1:
            return nums[0]

        s = 0
        e = n - 1

        while s <= e:
            mid = s + (e - s) // 2

            if mid == 0:
                if nums[mid] != nums[mid + 1]:
                    return nums[mid]

            elif mid == n - 1:
                if nums[mid] != nums[mid - 1]:
                    return nums[mid]

            elif nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    s = mid + 2
                else:
                    e = mid - 1
            else:
                if nums[mid] == nums[mid - 1]:
                    s = mid + 1
                else:
                    e = mid - 1
