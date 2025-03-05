class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        even_odd = False
        if(len(nums1) > len(nums2)):
            nums1,nums2 = nums2,nums1
        m = len(nums1)
        n = len(nums2)
        total_length = m + n

        if(total_length % 2 == 0):
            even_odd = True
        
        left = 0
        right = m
        

        while(left <= right):
            partition1 = (left + right ) // 2
            partition2 = ((m + n + 1) // 2) - partition1

            left1max = float('-inf') if partition1 == 0 else nums1[partition1-1]
            right1min = float('inf') if partition1 == m else nums1[partition1]
            
            left2max = float('-inf') if partition2 == 0 else nums2[partition2-1]
            right2min = float('inf') if partition2 == n else nums2[partition2]
            

            if left1max <= right2min and left2max <= right1min:
                if even_odd:
                    return (max(left1max,left2max)+min(right1min,right2min)) / 2
                else:
                    return float(max(left1max,left2max))
            elif left1max > right2min:
                right = partition1 - 1
            else:
                left  = partition1 + 1




        
        
