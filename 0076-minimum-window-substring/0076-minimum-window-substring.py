from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        needed = defaultdict(int)
        have = defaultdict(int)

        # Frequency of characters in t
        for ch in t:
            needed[ch] += 1

        left = 0
        start = 0
        min_len = float("inf")

        # Function to check whether current window is valid
        def sahi():
            for ch in needed:
                if have[ch] < needed[ch]:
                    return False
            return True

        # Expand window
        for right in range(len(s)):
            have[s[right]] += 1

            # Shrink window while it is valid
            while sahi():
                length = right - left + 1

                if length < min_len:
                    min_len = length
                    start = left

                have[s[left]] -= 1
                left += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]
        