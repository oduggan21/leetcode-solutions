class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if not s:
            return 0
       
        count = 0
        def expand(left, right,count):
            while(left >= 0 and right < n and s[left] == s[right]):
                count += 1
                left -=1
                right +=1
            return count
        
        for i in range(n):
            count +=  expand(i,i,0)
            count += expand(i,i+1,0)
        
        return count

