class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ''.join(filter(str.isalnum, s)).lower()
        return newString == newString[::-1]
