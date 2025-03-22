'''
# 48. Rotate Image

rotate 2d matrix 90 degree in place.
👉 transpose matrix and reverse each row.

- original matrix
1 2 3
4 5 6
7 8 9

- transpose matrix (swap i, j) (flip diagonally)
1 4 7
2 5 8
3 6 9

- reverse each row (horizontal flip)
7 4 1
8 5 2
9 6 3
'''
class Solution:
    '''
    TC: O(n^2)
    SC: O(1)
    '''
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()

'''
# 💡 other rotate in-place examples

## rotate 180 degree

### solution A. reverse each column (vertical flip) & reverse each row (horizontal flip)

```python
def rotate180(matrix: List[List[int]]) -> None:
  n = len(matrix)
  matrix.reverse()

  for i in range(n):
    matrix[i].reverse()
```

### solution B. (after transpose, reverse each row (horizontal flip)) * 2.

90 degree * 2 = 180 degree

```python
def rotate180(matrix: List[List[int]]) -> None:
  rotate90(matrix)
  rotate90(matrix)
```

## rotate -90 degree

after transpose, reverse each column (vertical flip)

```python
def rotate90CCW(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    matrix.reverse()
```
'''
