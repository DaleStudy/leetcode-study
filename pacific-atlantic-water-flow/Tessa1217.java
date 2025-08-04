import java.util.ArrayList;
import java.util.List;

class Solution {

    int[] dx = {1, -1, 0, 0};
    int[] dy = {0, 0, 1, -1};
    // boolean[][] visited;
    int width, height;

    // 시간복잡도, 공간복잡도: O(m * n)
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        height = heights.length;
        width = heights[0].length;

        boolean[][] pacific = new boolean[height][width];
        boolean[][] atlantic = new boolean[height][width];

        /**
         * 가장자리에 도달하는 경로를 일일이 탐색하는 것이 아닌 
         가장자리부터 물이 흐를 수 있는 경로를 역으로 탐색
         */

        // height check
        for (int i = 0; i < height; i++) {
            dfs(i, 0, heights, pacific);
            dfs(i, width - 1, heights, atlantic);
        }

        // width check
        for (int j = 0; j < width; j++) {
            dfs(0, j, heights, pacific);
            dfs(height - 1, j, heights, atlantic);
        }

        List<List<Integer>> answer = new ArrayList<>();
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    answer.add(List.of(i, j));
                }
            }
        }

        return answer;
    }

    private void dfs(int x, int y, int[][] heights, boolean[][] visited) {
        visited[x][y] = true;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && nx < height && ny >= 0 && ny < width) {
                if (!visited[nx][ny] && heights[nx][ny] >= heights[x][y]) {
                    dfs(nx, ny, heights, visited);
                }
            }
        }
    }

    // public List<List<Integer>> pacificAtlantic(int[][] heights) {
    //     height = heights.length;
    //     width = heights[0].length;
    //     visited = new boolean[height][width];

    //     List<List<Integer>> answer = new ArrayList<>();
    //     for (int i = 0; i < height; i++) {
    //         for (int j = 0; j < width; j++) {                
    //             WaterFlow checkWaterFlow = dfs(i, j, new WaterFlow(), heights);
    //             if (checkWaterFlow.crossBothOceans()) {
    //                 List<Integer> coordinate = List.of(i, j);                    
    //                 answer.add(coordinate);
    //             }
    //         }
    //     }
    //     return answer;
    // }

    // private WaterFlow dfs(int x, int y, WaterFlow checkWaterFlow, int[][] heights) {
    //     /**
    //     0, 0 | 0, 1 | 0, 2 | 0, 3 | 0, 4 
    //     1, 0 | 2, 0 | 3, 0 | 4, 0
    //         */
    //     if (x == 0 || y == 0) {
    //         checkWaterFlow.crossPacificFlow();
    //     }
    //     /**
    //     4, 0 | 4, 1 | 4, 2 | 4, 3 | 4, 4
    //     3, 4 | 2, 4 | 1, 4 | 0, 4
    //         */
    //     if (x == height - 1 || y == width - 1) {
    //         checkWaterFlow.crossAtlanticFlow();
    //     }

    //     if (checkWaterFlow.crossBothOceans()) {
    //         return checkWaterFlow;
    //     }

    //     visited[x][y] = true;

    //     for (int i = 0; i < 4; i++) {
    //         int nx = x + dx[i];
    //         int ny = y + dy[i];
    //         if (nx >= 0 && nx < height && ny >= 0 && ny < width) {
    //             if (!visited[nx][ny] && heights[nx][ny] <= heights[x][y]) {
    //                 dfs(nx, ny, checkWaterFlow, heights);            
    //             }                
    //         }            
    //     }
    //     visited[x][y] = false;

    //     return checkWaterFlow;
    // }

    // static class WaterFlow {

    //     private boolean pacificFlow;

    //     private boolean atlanticFlow;

    //     WaterFlow() {
    //         pacificFlow = false;
    //         atlanticFlow = false;
    //     }

    //     public void crossPacificFlow() {
    //         pacificFlow = true;
    //     }

    //     public void crossAtlanticFlow() {
    //         atlanticFlow = true;
    //     }

    //     public boolean crossBothOceans() {
    //         return pacificFlow && atlanticFlow;
    //     }

    // }
}

