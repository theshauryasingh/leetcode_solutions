class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0])-1
        print(row, col)
        while(col>=0 and col < len(matrix[0]) and row >=0 and row < len(matrix)):
            ele = matrix[row][col]
            print(ele)
            if ele == target:
                return True
            elif ele < target:
                row +=1
            elif ele > target:
                col -= 1
            print(row, col)
        return False
            
            
            
        