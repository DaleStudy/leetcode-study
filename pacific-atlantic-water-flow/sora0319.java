public class sora0319 {
    public class Solution {
        private int[][] heights;
        private int rows, cols;

        public List<List<Integer>> pacificAtlantic(int[][] heights) {
            this.heights = heights;
            this.rows = heights.length;
            this.cols = heights[0].length;
            List<List<Integer>> result = new ArrayList<>();

            for (int row = 0; row < rows; row++) {
                for (int col = 0; col < cols; col++) {
                    Set<String> visitedPac = new HashSet<>();
                    Set<String> visitedAtl = new HashSet<>();

                    if (dfsPac(row, col, visitedPac) && dfsAtl(row, col, visitedAtl)) {
                        result.add(Arrays.asList(row, col));
                    }
                }
            }
            return result;
        }

        private boolean dfsPac(int row, int col, Set<String> visited) {
            String key = row + "," + col;
            if (visited.contains(key)) return false;
            visited.add(key);

            if (row == 0 || col == 0) return true;

            int[][] moved = { {0, -1}, {0, 1}, {-1, 0}, {1, 0} };
            for (int[] m : moved) {
                int r = row + m[0];
                int c = col + m[1];
                if (isRange(r, c) && heights[row][col] >= heights[r][c]) {
                    if (dfsPac(r, c, visited)) return true;
                }
            }
            return false;
        }

        private boolean dfsAtl(int row, int col, Set<String> visited) {
            String key = row + "," + col;
            if (visited.contains(key)) return false;
            visited.add(key);

            if (row == rows - 1 || col == cols - 1) return true;

            int[][] directions = { {0, -1}, {0, 1}, {-1, 0}, {1, 0} };
            for (int[] dir : directions) {
                int r = row + dir[0];
                int c = col + dir[1];
                if (isRange(r, c) && heights[row][col] >= heights[r][c]) {
                    if (dfsAtl(r, c, visited)) return true;
                }
            }
            return false;
        }

        private boolean isRange(int r, int c) {
            return r >= 0 && r < rows && c >= 0 && c < cols;
        }
    }

}

