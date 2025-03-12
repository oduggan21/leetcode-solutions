class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0

        fast = nums[nums[fast]]
        slow = nums[slow]

        while(1):
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
                
        slow = 0 
        while(slow != fast):
            slow = nums[slow]
            fast = nums[fast]

        return slow 
