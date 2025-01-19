// 처음보는 시뮬레이션 문제라 그냥 풀었음
// 별다른 알고리즘이 필요없다.
public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        if (matrix == null || matrix.length == 0) return result;

        int rows = matrix.length;
        int cols = matrix[0].length;
        boolean[][] visited = new boolean[rows][cols];

        int[] dRow = {0, 1, 0, -1};
        int[] dCol = {1, 0, -1, 0};

        int row = 0, col = 0, dir = 0;

        for (int i = 0; i < rows * cols; i++) {
            result.add(matrix[row][col]);
            visited[row][col] = true;

            int nextRow = row + dRow[dir];
            int nextCol = col + dCol[dir];

            if (nextRow < 0 || nextRow >= rows || nextCol < 0 || nextCol >= cols || visited[nextRow][nextCol]) {
                dir = (dir + 1) % 4;
                nextRow = row + dRow[dir];
                nextCol = col + dCol[dir];
            }

            row = nextRow;
            col = nextCol;
        }

        return result;
    }
}
