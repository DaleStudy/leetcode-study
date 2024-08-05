- 문제: https://leetcode.com/problems/set-matrix-zeroes/
- 풀이: https://algorithm.jonghoonpark.com/2024/02/16/leetcode-73

## 처음 생각난 방법

```java
class Solution {
    public void setZeroes(int[][] matrix) {
        List<Index> indexOfZero = new ArrayList<>();

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    indexOfZero.add(new Index(i, j));
                }
            }
        }

        for (Index index : indexOfZero) {
            // update row
            Arrays.fill(matrix[index.i], 0);

            // update column
            for (int i = 0; i < matrix.length; i++) {
                matrix[i][index.j] = 0;
            }
        }
    }
}

class Index {
    int i;
    int j;

    public Index(int i, int j) {
        this.i = i;
        this.j = j;
    }
}
```

### TC, SC

문제에서 m과 n이 다음과 같이 정의되어 있다.

```
m == matrix.length
n == matrix[0].length
```

시간복잡도는 `O(n * m)` 공간복잡도는 `O(n * m)` 이다.

## simple improvement

```java
class Solution {
    public void setZeroes(int[][] matrix) {
        int[] row = new int[matrix.length];
        int[] col = new int[matrix[0].length];

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    row[i] = 1;
                    col[j] = 1;
                }
            }
        }

        // update row
        for (int i = 0; i < row.length; i++) {
            if (row[i] == 1) {
                Arrays.fill(matrix[i], 0);
            }
        }

        // update column
        for (int j = 0; j < col.length; j++) {
            if (col[j] == 1) {
                for (int i = 0; i < matrix.length; i++) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
}
```

#### TC, SC

문제에서 m과 n이 다음과 같이 정의되어 있다.

```
m == matrix.length
n == matrix[0].length
```

시간복잡도는 `O(n * m)` 공간복잡도는 `O(n + m)` 이다. 공간 복잡도가 개선되었다.

## in place 방식으로 접근해보기

문제를 자세히 읽어보면 [in place](https://en.wikipedia.org/wiki/In-place_algorithm) 방식으로 풀라고 되어있다.

```java
class Solution {
    public void setZeroes(int[][] matrix) {
        boolean shouldUpdateFirstRow = false;
        boolean shouldUpdateFirstColumn = false;

        for (int i = 0; i < matrix.length; i++) {
            if (matrix[i][0] == 0) {
                shouldUpdateFirstColumn = true;
                break;
            }
        }

        for (int j = 0; j < matrix[0].length; j++) {
            if (matrix[0][j] == 0) {
                shouldUpdateFirstRow = true;
                break;
            }
        }

        for (int i = 1; i < matrix.length; i++) {
            for (int j = 1; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        // update row
        for (int i = 1; i < matrix.length; i++) {
            if (matrix[i][0] == 0) {
                Arrays.fill(matrix[i], 0);
            }
        }

        // update column
        for (int j = 1; j < matrix[0].length; j++) {
            if (matrix[0][j] == 0) {
                for (int i = 0; i < matrix.length; i++) {
                    matrix[i][j] = 0;
                }
            }
        }

        // update first row if contains zero
        if (shouldUpdateFirstRow) {
            Arrays.fill(matrix[0], 0);
        }

        // update first column if contains zero
        if (shouldUpdateFirstColumn) {
            for (int i = 0; i < matrix.length; i++) {
                matrix[i][0] = 0;
            }
        }
    }
}
```

#### TC, SC

문제에서 m과 n이 다음과 같이 정의되어 있다.

```
m == matrix.length
n == matrix[0].length
```

시간복잡도는 `O(n * m)` 공간복잡도는 `O(1)` 이다. 공간 복잡도가 한 번 더 개선되었다.
