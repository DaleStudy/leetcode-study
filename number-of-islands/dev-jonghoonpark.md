- 문제: https://leetcode.com/problems/number-of-islands/
- 풀이: https://algorithm.jonghoonpark.com/2024/03/31/leetcode-200

```java
class Solution {
    public int numIslands(char[][] grid) {
        int w = grid.length;
        int h = grid[0].length;

        int count = 0;
        for (int i = 0; i < w; i++) {
            for (int j = 0; j < h; j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i,j);
                    count++;
                }
            }
        }
        return count;
    }

    public void dfs(char[][] grid, int i, int j) {
        if(i < 0 || i >= w || j < 0 || j >= h || grid[i][j] == '0') {
            return;
        }

        grid[i][j] = '0';

        dfs(grid, i-1, j);
        dfs(grid, i, j-1);
        dfs(grid, i+1, j);
        dfs(grid, i, j+1);
    }
}
```

## TC, SC

코드에 정의한 대로 grid의 길이를 `w`, grid[0]의 길이를 `h`로 정의했을 때,
이 코드의 시간 복잡도는 O(w \* h), 공간 복잡도는 O(w \* h) 이다.
