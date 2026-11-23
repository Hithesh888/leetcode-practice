
class Solution(object):
    def searchMatrix(self, mat, target):
        m = len(mat)
        n = len(mat[0])

        st = 0
        en = m - 1

        while st <= en:
            mid = (st + en) // 2

            if mat[mid][0] <= target <= mat[mid][n-1]:
                return self.findNumber(mat[mid], target)

            elif mat[mid][0] > target:
                en = mid - 1

            else:
                st = mid + 1

        return False

    def findNumber(self, arr, target):
        s = 0
        e = len(arr) - 1

        while s <= e:
            mid = (s + e) // 2

            if arr[mid] == target:
                return True

            elif arr[mid] > target:
                e = mid - 1

            else:
                s = mid + 1

        return False
