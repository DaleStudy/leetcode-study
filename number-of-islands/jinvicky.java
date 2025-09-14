public class jinvicky {
}

/**
 * 일관성을 위해 모든 변수들을 메서드 내 lv로 선언해서 푸는 것으로 한다.
 * dfs를 설계할 때 특히 반환 타입에 약한데 void인가 int,booelan 등 기타 타입인가를 확실히 하기 위해 별도 예제로 풀었다.
 * 또한 의도적으로 기존 grid를 1 -> 0으로 바꾸어 섬을 없애지 않고 공간복잡도가 증가하더라도 학습을 위해 방문 배열을 별도로 선언해 방문 여부를 체크했다.
 */
class Solution {
    public int numIslands1(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        int rows = grid.length, cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];

        int count = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1' && !visited[r][c]) {
                    int size = dfsByInt(grid, visited, r, c, rows, cols);
                    if (size > 0) count++; // 크기가 양수면 섬 1개
                }
            }
        }
        return count;
    }

    // dfs는 해당 섬의 넓이를 반환
    private int dfsByInt(char[][] grid, boolean[][] visited, int r, int c, int rows, int cols) {
        if (r < 0 || c < 0 || r >= rows || c >= cols) return 0; // 범위를 벗어났다.
        if (grid[r][c] == '0' || visited[r][c]) return 0; // 문제의 조건에 맞지 않거나, 이미 방문했다.

        visited[r][c] = true; // 방문 처리
        int area = 1;

        area += dfsByInt(grid, visited, r + 1, c, rows, cols);
        area += dfsByInt(grid, visited, r - 1, c, rows, cols);
        area += dfsByInt(grid, visited, r, c + 1, rows, cols);
        area += dfsByInt(grid, visited, r, c - 1, rows, cols);

        return area;
    }

    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        int rows = grid.length, cols = grid[0].length;

        boolean[][] visited = new boolean[rows][cols];
        int count = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1' && !visited[r][c]) {
                    dfs(grid, visited, r, c, rows, cols);
                    count++; // 섬 하나 탐색 끝나면 +1
                }
            }
        }
        return count;
    }

    private void dfs(char[][] grid, boolean[][] visited, int r, int c, int rows, int cols) {
        if (r < 0 || c < 0 || r >= rows || c >= cols) return; // 그리드 범위를 벗어나면 종료
        if (grid[r][c] == '0' || visited[r][c]) return; // 물이거나 이미 방문한 섬이라면 종료

        visited[r][c] = true; // 방문 처리

        // 상하좌우 DFS
        dfs(grid, visited, r + 1, c, rows, cols);
        dfs(grid, visited, r - 1, c, rows, cols);
        dfs(grid, visited, r, c + 1, rows, cols);
        dfs(grid, visited, r, c - 1, rows, cols);
    }

    /**
     * void 반환의 dfs면 return;
     * int 반환의 dfs면 return 0;
     * bool 반환의 dfs면 return false;
     *
     * 1. 리턴값 없이 넘겨받은 상태만 갱신
     * void dfs(Node node) {
     *     if (범위 밖 || 조건 불만족 || 이미 방문) return;
     *
     *     방문 처리(node);
     *
     *     for (이웃 nei : node) {
     *         dfs(nei);
     *     }
     * }
     *
     * 2. 최대/최소 값을 정수로 반환
     * int dfs(Node node) {
     *     if (범위 밖 || 조건 불만족) return 0;
     *
     *     방문 처리(node);
     *
     *     int result = 1; // 자기 자신 포함
     *     for (이웃 nei : node) {
     *         result += dfs(nei);
     *     }
     *     return result;
     * }
     * 3. 조건 만족 여부
     * boolean dfs(Node node) {
     *     if (목표 도달) return true;
     *     if (범위 밖 || 조건 불만족) return false;
     *
     *     방문 처리(node);
     *
     *     for (이웃 nei : node) {
     *         if (dfs(nei)) return true;
     *     }
     *     return false;
     * }
     *
     * 4. 메모이제이션/DP 결합
     * int dfs(Node node, Map<Node,Integer> memo) {
     *     if (memo.containsKey(node)) return memo.get(node);
     *     if (기저 조건) return 1;
     *
     *     int best = 0;
     *     for (이웃 nei : node) {
     *         best = Math.max(best, 1 + dfs(nei, memo));
     *     }
     *     memo.put(node, best);
     *     return best;
     * }
     */
}
