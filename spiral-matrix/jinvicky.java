import java.util.*;

/**
 * dir[][]의 방향을 나선으로 맞추는 것이 가장 중요. 단순 dfs, bfs의 4방향이 아님.
 */
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ans = new ArrayList<>();
        int m = matrix.length;
        if (m == 0) return ans;
        int n = matrix[0].length;

        boolean[][] visited = new boolean[m][n];

        // 한 배열에 (row, col) 방향쌍을 보관: → ↓ ← ↑
        int[][] dir = {{0,1}, {1,0}, {0,-1}, {-1,0}};
        int d = 0;          // 현재 방향 인덱스
        int i = 0, j = 0;   // 현재 위치

        for (int k = 0; k < m * n; k++) {
            ans.add(matrix[i][j]);
            visited[i][j] = true;

            int ni = i + dir[d][0];
            int nj = j + dir[d][1];

            // 경계 밖이거나 이미 방문했다면 방향 전환
            if (ni < 0 || ni >= m || nj < 0 || nj >= n || visited[ni][nj]) {
                d = (d + 1) % 4;   // 0→1→2→3→0
                ni = i + dir[d][0];
                nj = j + dir[d][1];
            }

            i = ni; j = nj;
        }
        return ans;
    }
}
