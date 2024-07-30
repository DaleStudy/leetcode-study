- 문제: https://leetcode.com/problems/spiral-matrix/
- 풀이: https://algorithm.jonghoonpark.com/2024/07/30/leetcode-54

```java
class Solution {

    final int VISITED = 101;

    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ordered = new ArrayList<>();

        int i = 0;
        int j = 0;
        int depth = 0; // 한 바퀴 돌 때 마다 안쪽으로 들어가게 됨.

        int startI = Integer.MIN_VALUE;
        int startJ = Integer.MIN_VALUE;

        while (!(i == startI && j == startJ)) {
            startI = i;
            startJ = j;

            // 마지막에서 i++ 을 진행하는데 이로 인해서 범위를 초과하는 것을 방지
            if (i == matrix.length) {
                break;
            }

            // 오른쪽으로 이동
            while (j < matrix[0].length - depth) {
                update(matrix, i, j, ordered);
                j++;
            }
            j--;

            // 아래로 이동
            while (i < matrix.length - depth) {
                update(matrix, i, j, ordered);
                i++;
            }
            i--;

            // 왼쪽으로 이동
            while (j > depth - 1) {
                update(matrix, i, j, ordered);
                j--;
            }
            j++;

            // 위로 이동
            while (i > depth - 1) {
                update(matrix, i, j, ordered);
                i--;
            }
            i++;

            // while 조건에 걸리지 않도록 다음 칸으로 이동
            i++;
            j++;

            depth++;
        }

        return ordered;
    }

    private void update(int[][] matrix, int i, int j, List<Integer> ordered) {
        if (i < 0 || j < 0 || i >= matrix.length || j >= matrix[0].length) {
            return;
        }

        if (matrix[i][j] != VISITED) {
            ordered.add(matrix[i][j]);
        }
        matrix[i][j] = VISITED;
    }
}
```

## TC, SC

n은 matrix의 모든 아이템의 수를 한다고 하였을 때, 시간복잡도는 `O(n)`, 공간복잡도는 `O(1)` 이다. (공간복잡도의 경우 결과를 위해 생성되는 List는 계싼에서 제외함.)
