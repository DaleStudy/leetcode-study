// TC: O(n * m)
// visit all elements
// SC: O(n * m)
// create result from all elements
class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> output = new ArrayList<>();

        if (heights.length == 0 || heights[0].length == 0) return output;

        int rows = heights.length;
        int cols = heights[0].length;

        boolean[][] pac = new boolean[rows][cols];
        boolean[][] atl = new boolean[rows][cols];

        for (int j = 0; j < rows; j++) {
            dfs(j, 0, pac, heights[j][0], heights);
            dfs(j, cols-1, atl, heights[j][cols-1], heights);
        }

        for (int i = 0; i < cols; i++) {
            dfs(0, i, pac, heights[0][i], heights);
            dfs(rows-1, i, atl, heights[rows-1][i], heights);
        }

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (pac[i][j] && atl[i][j]) output.add(List.of(i,j));
            }
        }
        return output;
    }

    private void dfs(int i, int j, boolean[][] visit, int preValue, int[][] heights) {
        if (i < 0 || j < 0 || i == heights.length || j == heights[0].length || visit[i][j] || preValue > heights[i][j]) return;

        visit[i][j] = true;
        dfs(i + 1, j, visit, heights[i][j], heights);
        dfs(i - 1, j, visit, heights[i][j], heights);
        dfs(i, j + 1, visit, heights[i][j], heights);
        dfs(i, j - 1, visit, heights[i][j], heights);
    }
}
