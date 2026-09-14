class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

solution = Solution()
print(solution.longestConsecutive([100,4,200,1,3,2]))

# https://leetcode.com/problems/longest-consecutive-sequence/description/