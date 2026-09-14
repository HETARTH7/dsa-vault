class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        i = 0
        longestSubstring = 0
        for j in range(len(s)):
            newChar = s[j]
            while newChar in letters:
                letters.remove(s[i])
                i += 1
            longestSubstring = max(longestSubstring, j - i + 1)
            letters.add(newChar)
        return longestSubstring

solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))

# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/