class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums) -1

        def binarySearch(nums, target, low, high):

            if high >= low:

                mid = (low + high) // 2

                if(nums[mid] == target):
                    return mid
                elif(nums[mid] > target):
                    return binarySearch(nums, target,low, mid -1)
                else:
                    return binarySearch(nums, target, mid+1, high)
            else:
                return -1
            
        num = binarySearch(nums, target, low, high)
        return num
        
