from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freq = Counter(t)
        result_start = 0
        required = len(t)
        left = 0
        min_length = float('inf')

        for right, ch in enumerate(s):
            
            if freq[ch] > 0:
                required -= 1
            
            freq[ch] -= 1

            while required == 0:
                if(right-left+1 < min_length):
                    result_start = left
                    min_length = right-left+1
                letter = s[left]
                if letter in freq:
                    freq[letter] += 1
                if freq[letter] > 0:
                    required += 1
                left += 1
        
        return "" if min_length == float('inf') else s[result_start:result_start+min_length]


        
