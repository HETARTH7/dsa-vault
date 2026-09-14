from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = defaultdict(int)

        for char in t:
            tmap[char] += 1

        smap = defaultdict(int)

        left = 0
        right = 0

        required = len(tmap)
        formed = 0

        best_start = 0
        best_len = float("inf")

        while right < len(s):
            char = s[right]
            smap[char] += 1

            if char in tmap and smap[char] == tmap[char]:
                formed += 1

            while formed == required:
                window_len = right - left + 1

                if window_len < best_len:
                    best_len = window_len
                    best_start = left

                left_char = s[left]
                smap[left_char] -= 1

                if left_char in tmap and smap[left_char] < tmap[left_char]:
                    formed -= 1

                left += 1

            right += 1

        if best_len == float("inf"):
            return ""

        return s[best_start:best_start + best_len]


solution = Solution()
print(solution.minWindow("ab", "a"))


# https://leetcode.com/problems/minimum-window-substring/