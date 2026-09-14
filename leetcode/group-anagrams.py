from collections import defaultdict

class Solution:
    def getKey(self, string: str) -> str:
        return "".join(sorted(string))

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            key = self.getKey(string)
            # print(key)
            anagrams[key].append(string)
        # print(anagrams)
        return list(anagrams.values())

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# https://leetcode.com/problems/group-anagrams/description/