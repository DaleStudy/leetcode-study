import java.util.ArrayList;
import java.util.List;

class Solution {
    static int[][] MOVES = {
            {1, 0}, {-1, 0}, {0, 1}, {0, -1}
    };

    static void dfs(int[][] heights, boolean[][] visited, int i, int j) {
        visited[i][j] = true;

        for (int[] move : MOVES) {
            int next_i = i + move[0];
            int next_j = j + move[1];

            if (next_i < 0 || next_i >= heights.length
                    || next_j < 0 || next_j >= heights[0].length) {
                continue;
            }

            if (visited[next_i][next_j]) {
                continue;
            }

            // 바다에서 역방향으로 올라가므로
            // 현재 높이보다 높거나 같은 곳으로만 이동
            if (heights[next_i][next_j] < heights[i][j]) {
                continue;
            }

            dfs(heights, visited, next_i, next_j);
        }
    }

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int rows = heights.length;
        int cols = heights[0].length;

        boolean[][] po = new boolean[rows][cols];
        boolean[][] ao = new boolean[rows][cols];

        // 위 / 아래
        for (int j = 0; j < cols; j++) {
            dfs(heights, po, 0, j);
            dfs(heights, ao, rows - 1, j);
        }

        // 왼쪽 / 오른쪽
        for (int i = 0; i < rows; i++) {
            dfs(heights, po, i, 0);
            dfs(heights, ao, i, cols - 1);
        }

        List<List<Integer>> answer = new ArrayList<>();

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (po[i][j] && ao[i][j]) {
                    answer.add(List.of(i, j));
                }
            }
        }

        return answer;
    }
}
