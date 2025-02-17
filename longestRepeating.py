class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       freq = {} 
       result = 0
       start = 0
       maxCount = 0

       for end, ch in enumerate(s):
            character = s[end]
            freq[character] = freq.get(character, 0) + 1
            maxCount = max(maxCount, freq[character])

            while(end-start+1-maxCount > k):
                letter = s[start]
                freq[letter] -= 1
                start +=1
            result = max(result, end-start+1)
       return result
