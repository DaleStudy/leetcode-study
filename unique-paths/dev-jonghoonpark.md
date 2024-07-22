- 문제: https://leetcode.com/problems/unique-paths/
- 풀이: https://algorithm.jonghoonpark.com/2024/07/16/leetcode-62

```java
class Solution {
    public int uniquePaths(int m, int n) {
        int[][] matrix = new int[m][n];
        matrix[0][0] = 1;

        Deque<Coordinate> deque = new ArrayDeque<>();
        deque.addLast(new Coordinate(1, 0));
        deque.addLast(new Coordinate(0, 1));
        while (!deque.isEmpty()) {
            Coordinate coordinate = deque.removeFirst();
            if (coordinate.x >= m || coordinate.y >= n || matrix[coordinate.x][coordinate.y] != 0) {
                continue;
            }

            int top = coordinate.y > 0 ? matrix[coordinate.x][coordinate.y - 1] : 0;
            int left = coordinate.x > 0 ? matrix[coordinate.x - 1][coordinate.y] : 0;
            matrix[coordinate.x][coordinate.y] = top + left;

            deque.addLast(new Coordinate(coordinate.x + 1, coordinate.y));
            deque.addLast(new Coordinate(coordinate.x, coordinate.y + 1));
        }

        return matrix[m - 1][n - 1];
    }
}

class Coordinate {
    int x;
    int y;

    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
```

### TC, SC

시간 복잡도는 `O(m * n)` 공간 복잡도는 `O(m * n)` 이다.
