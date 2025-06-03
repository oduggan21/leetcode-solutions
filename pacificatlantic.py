class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # if we are at row 0 or column 0 we can flow into pacific 
        # if we are at len(heights) - 1 of len(heights[0]) - 1 then we can flow into atlantic

        def dfsAtlantic(row,col,visited):
        
            if (row,col) in visited:
                return False
            if row == len(heights)-1 or col == len(heights[0])-1:
                return True
            visited.add((row,col))
            if row - 1 >= 0 and heights[row-1][col] <= heights[row][col] and dfsAtlantic(row-1,col,visited):
                return True
            if col - 1 >= 0 and heights[row][col-1] <= heights[row][col] and dfsAtlantic(row,col-1,visited):
                return True
            if row + 1 < len(heights) and heights[row+1][col] <= heights[row][col] and dfsAtlantic(row+1,col,visited):
                return True
            if col + 1 < len(heights[0]) and heights[row][col+1] <= heights[row][col] and dfsAtlantic(row,col+1,visited):
                return True
            
            return False
        
        def dfsPacific(row,col,visited):
            
            if (row,col) in visited:
                return False
            if row == 0 or col == 0:
                return True
            visited.add((row,col))
            if row-1 >= 0 and heights[row-1][col] <= heights[row][col] and dfsPacific(row-1,col,visited):
                return True
            if col -1 >= 0 and heights[row][col-1] <= heights[row][col] and dfsPacific(row,col-1,visited):
                return True
            if row + 1 < len(heights) and heights[row+1][col] <= heights[row][col] and dfsPacific(row+1,col,visited):
                return True
            if col+1 < len(heights[0]) and heights[row][col+1] <= heights[row][col] and dfsPacific(row,col+1,visited):
                return True
            
            return False
        final_list = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if dfsAtlantic(row,col,set()) and dfsPacific(row,col,set()):
                    final_list.append([row,col])
        return final_list
