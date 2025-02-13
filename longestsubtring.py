class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            last_index = {}
            length = 0
            start = 0

            for i, ch in enumerate(s):
                if (ch in last_index) and last_index[ch] >= start:
                    start = last_index[ch] + 1
                last_index[ch] = i
                length = max(length, i-start + 1)
            return length
