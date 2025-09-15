import java.util.ArrayList;
import java.util.List;

class Solution {
    private int[][] heights;
    private int rows, cols;
    private int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}}; // 상하좌우

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        this.heights = heights;
        this.rows = heights.length;
        this.cols = heights[0].length;

        // 태평양과 대서양에서 도달 가능한 지점을 저장하는 배열
        boolean[][] pacific = new boolean[rows][cols];
        boolean[][] atlantic = new boolean[rows][cols];

        // 태평양과 대서양 경계에서 탐색 시작
        // 맨 윗줄과 맨 아랫줄
        for (int j = 0; j < cols; j++) {
            dfs(0, j, pacific, Integer.MIN_VALUE);      // 태평양 (윗줄)
            dfs(rows - 1, j, atlantic, Integer.MIN_VALUE); // 대서양 (아랫줄)
        }

        // 맨 왼쪽줄과 맨 오른쪽줄
        for (int i = 0; i < rows; i++) {
            dfs(i, 0, pacific, Integer.MIN_VALUE);      // 태평양 (왼쪽줄)
            dfs(i, cols - 1, atlantic, Integer.MIN_VALUE); // 대서양 (오른쪽줄)
        }

        // 결과를 저장할 리스트
        List<List<Integer>> result = new ArrayList<>();

        // 양쪽 바다로 모두 흐를 수 있는 지점 찾기
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    List<Integer> coord = new ArrayList<>();
                    coord.add(i);
                    coord.add(j);
                    result.add(coord);
                }
            }
        }

        return result;
    }

    // 깊이 우선 탐색 (DFS) 함수
    private void dfs(int r, int c, boolean[][] visited, int prevHeight) {
        // 유효하지 않은 지점 (범위 밖, 이미 방문, 높이 조건 불만족)
        if (r < 0 || r >= rows || c < 0 || c >= cols || visited[r][c] || heights[r][c] < prevHeight) {
            return;
        }

        // 현재 지점 방문 표시
        visited[r][c] = true;

        // 상하좌우로 탐색 진행
        for (int[] dir : directions) {
            int newR = r + dir[0];
            int newC = c + dir[1];
            dfs(newR, newC, visited, heights[r][c]);
        }
    }
}
