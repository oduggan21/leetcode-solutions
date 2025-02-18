from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        freq = Counter(s1)
        window = Counter(s2[:len(s1)])

        if window == freq:
            return True

        for i in range(len(s1), len(s2)):
            window[s2[i]] += 1

            left_char = s2[i-len(s1)]
            window[left_char] -= 1
            
            if(window[left_char] == 0):
                del window[left_char]
            
            if window == freq:
                return True 
        
        return False


        
