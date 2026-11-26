
class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        a = 0
        b = 0
        s = set()
        actualSum = 0
        expectedSum = 0

        for i in range(n):
            for j in range(n):
                actualSum += grid[i][j]

                if grid[i][j] in s:
                    a = grid[i][j]

                s.add(grid[i][j])

        expectedSum = (n*n * (n*n+1)) // 2
        b = expectedSum + a - actualSum

        return [a, b]
