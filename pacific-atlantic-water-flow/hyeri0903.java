class Solution {
    int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        /**
        1.2개의 ocean 모두로 도달할 수 있는 칸들을 찾는 문제
        2.height 높은 곳 -> 낮은 곳으로 이동
        time, space: O(mn)
         */
         int m = heights.length;
         int n = heights[0].length;
         boolean[][] pacific = new boolean[m][n];
         boolean[][] atlantic = new boolean[m][n];

         List<List<Integer>> answer = new ArrayList<>();

        for(int i = 0; i < m; i++) {
            dfs(i, 0, m, n, heights, pacific);
            dfs(i, n-1, m, n, heights, atlantic);
        }
        for(int j = 0; j < n; j++) {
            dfs(0, j, m, n, heights, pacific);
            dfs(m-1, j, m, n, heights, atlantic);
        }

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(pacific[i][j] && atlantic[i][j]) {
                    answer.add(Arrays.asList(i,j));
                }
            }
        }
        return answer;
    }

    void dfs(int i, int j, int m, int n, int[][] heights, boolean[][] visited) {
        if(i < 0 || i >= m || j < 0 || j >= n || visited[i][j]) {
            return;
        }

        visited[i][j] = true;
        for(int[] d: dirs) {
            int nexti = i + d[0];
            int nextj = j + d[1];

            //범위 안 && 방문 안했고 && 높이 조건 만족하면 다음 루트 탐색
            if(nexti >= 0 && nexti < m && nextj >= 0 && nextj < n && !visited[nexti][nextj] && heights[nexti][nextj] >= heights[i][j]) {
                dfs(nexti, nextj, m, n, heights, visited);
            }

        }
    }
}
