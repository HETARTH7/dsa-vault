class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev = {}
        for i, num in enumerate(nums):
            required = target - num
            if required in prev:
                return [prev[required], i]
            prev[num] = i
        return []

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))

# https://leetcode.com/problems/two-sum/description/