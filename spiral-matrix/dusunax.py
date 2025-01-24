'''
# 54. Spiral Matrix

to traverse the matrix in a spiral order:
1. do boundary-tracking
2. iterate in layers
  - move right, move down, move left, move up
  - shrink the boundaries
4. return the result

# Time and Space Complexity

```
TC: O(m * n)
SC: O(1)
```

#### TC is O(m * n):
move through the 2D matrix just once. = O(m * n)

#### SC is O(1):
result list is excluded from auxiliary space, so it's = O(1)
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        result = [] # SC: O(1)

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result
