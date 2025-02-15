// 개인적으로 행렬에서 전파되는 방식은 BFS를 이용한 구현 방식을 선호한다.
// 최적의 실행시간이 나오지 않는 것 같아서 DFS로 선회
class Solution {
    private int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    private int m, n;

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        m = heights.length;
        n = heights[0].length;
        
        boolean[][] pacific = new boolean[m][n];
        boolean[][] atlantic = new boolean[m][n];
        List<List<Integer>> result = new ArrayList<>();

        
        for (int i = 0; i < m; i++) {
            dfs(heights, pacific, i, 0);
            dfs(heights, atlantic, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            dfs(heights, pacific, 0, j);
            dfs(heights, atlantic, m - 1, j);
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    result.add(Arrays.asList(i, j));
                }
            }
        }

        return result;
    }

    private void dfs(int[][] heights, boolean[][] visited, int x, int y) {
        visited[x][y] = true;
        for (int[] dir : directions) {
            int newX = x + dir[0], newY = y + dir[1];
            if (newX >= 0 && newX < m && newY >= 0 && newY < n && !visited[newX][newY] && heights[newX][newY] >= heights[x][y]) { 
                dfs(heights, visited, newX, newY);
            }
        }
    }
}

class Solution {
    private int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    private int m, n;

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        m = heights.length;
        n = heights[0].length;
        
        boolean[][] pacific = new boolean[m][n];
        boolean[][] atlantic = new boolean[m][n];
        List<List<Integer>> result = new ArrayList<>();

        Queue<int[]> pacificQueue = new LinkedList<>();
        Queue<int[]> atlanticQueue = new LinkedList<>();
        
        for (int i = 0; i < m; i++) {
            pacificQueue.offer(new int[]{i, 0});
            atlanticQueue.offer(new int[]{i, n - 1});
            pacific[i][0] = true;
            atlantic[i][n - 1] = true;
        }
        for (int j = 0; j < n; j++) {
            pacificQueue.offer(new int[]{0, j});
            atlanticQueue.offer(new int[]{m - 1, j});
            pacific[0][j] = true;
            atlantic[m - 1][j] = true;
        }

        bfs(heights, pacificQueue, pacific);
        bfs(heights, atlanticQueue, atlantic);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    result.add(Arrays.asList(i, j));
                }
            }
        }

        return result;
    }

    private void bfs(int[][] heights, Queue<int[]> queue, boolean[][] visited) {
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int x = cell[0], y = cell[1];

            for (int[] dir : directions) {
                int newX = x + dir[0], newY = y + dir[1];
                if (newX >= 0 && newX < m && newY >= 0 && newY < n && !visited[newX][newY] && heights[newX][newY] >= heights[x][y]) {
                    queue.offer(new int[]{newX, newY});
                    visited[newX][newY] = true;
                }
            }
        }
    }
}
