from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        sumCnt = defaultdict(int)
        currSum, cnt = 0, 0
        for num in nums:
            sumCnt[currSum] += 1
            currSum += num
            cnt += sumCnt[currSum - k]
        return cnt

solution = Solution()
print(solution.subarraySum([1,1,1], 2))
# https://leetcode.com/problems/subarray-sum-equals-k/