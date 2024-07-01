/*
 * time: O(M*N)
 * space: O(M*N)
 *  - M is the number of rows
 *  - N is the number of columns
 */
class Solution {

    int[][] heights;
    int rLen;
    int cLen;
    int[] rDirs = {0, -1, 0, 1};
    int[] cDirs = {1, 0, -1, 0};

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        this.heights = heights;
        this.rLen = heights.length;
        this.cLen = heights[0].length;

        boolean[][] pacific = new boolean[rLen][cLen];
        boolean[][] atlantic = new boolean[rLen][cLen];

        for (int i = 0; i < rLen; i++) {
            dfs(i, 0, pacific);
            dfs(i, cLen - 1, atlantic);
        }

        for (int i = 0; i < cLen; i++) {
            dfs(0, i, pacific);
            dfs(rLen - 1, i, atlantic);
        }

        List<List<Integer>> both = new ArrayList<>();
        for (int i = 0; i < rLen; i++) {
            for (int j = 0; j < cLen; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    both.add(List.of(i, j));
                }
            }
        }
        return both;
    }

    private void dfs(int r, int c, boolean[][] visited) {
        visited[r][c] = true;

        for (int d = 0; d < 4; d++) {
            int nr = r + rDirs[d];
            int nc = c + cDirs[d];

            if (nr < 0 || nr > rLen - 1 || nc < 0 || nc > cLen - 1) {
                continue;
            }

            if (visited[nr][nc]) {
                continue;
            }

            if (heights[nr][nc] < heights[r][c]) {
                continue;
            }

            dfs(nr, nc, visited);
        }
    }
}
