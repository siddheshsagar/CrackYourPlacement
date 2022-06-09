# Leetcode Problem 54. Spiral Matrix
# Problem Link : https://leetcode.com/problems/spiral-matrix/

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        top = 0
        right = len(matrix[0])
        bottom = len(matrix)
        lis = []
        
        while left < right and top < bottom:
            for i in range(left,right):
                lis.append(matrix[top][i])
            top += 1
            
            for i in range(top,bottom):
                lis.append(matrix[i][right-1])
            right -= 1
            
            if not (left < right and top < bottom):
                break
            
            for i in range(right-1,left-1,-1):
                lis.append(matrix[bottom-1][i])
            bottom -= 1
                
            for i in range(bottom-1,top-1,-1):
                lis.append(matrix[i][left])
            left += 1
            
        return lis
                
