class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows*cols - 1

        while(left<= right):
            mid= (left + right) // 2
            row = mid // cols ##we divide mid by columns to now how many rows we have iterated over
            #if mid = 5, and we have 4 columns, then we have gone over 1 row
            col = mid % cols ##the remainder tells us what column we are at in the specific row

            if(matrix[row][col] == target):
                return True
            elif(matrix[row][col] < target):
                left = mid + 1
            else:
                right = mid - 1
        
        return False
        
