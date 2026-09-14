class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2

        return max(x1, x3) < min(x2, x4) and \
               max(y1, y3) < min(y2, y4)

solution = Solution()
print(solution.isRectangleOverlap([0,0,2,2], [1,1,3,3]))
print(solution.isRectangleOverlap([0,0,1,1], [1,0,2,1]))
print(solution.isRectangleOverlap([0,0,1,1], [2,2,3,3]))

# https://leetcode.com/problems/rectangle-overlap/description/
# Time- O(1)
# Space- O(1)