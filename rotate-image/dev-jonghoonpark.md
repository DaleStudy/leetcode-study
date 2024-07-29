- 문제: https://leetcode.com/problems/rotate-image/
- 풀이: https://algorithm.jonghoonpark.com/2024/07/22/leetcode-48

```java
class Solution {
    public void rotate(int[][] matrix) {
        int l = matrix.length;

        int limit = (int) Math.ceil((double) l / 2);
        for (int i = 0; i < limit; i++) {
            for (int j = i; j < l - 1 - i; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[l - j - 1][i];
                matrix[l - j - 1][i] = matrix[l - i - 1][l - j - 1];
                matrix[l - i - 1][l - j - 1] = matrix[j][l - i - 1];
                matrix[j][l - i - 1] = temp;
            }
        }
    }
}
```

### TC, SC

시간 복잡도는 `O(n^2)` 공간 복잡도는 `O(1)` 이다.
