// time: O(m*n)
// space: O(m*n)
class Solution {

    public List<Integer> spiralOrder(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int dir = 1;
        int i = 0;
        int j = -1;

        List<Integer> output = new ArrayList<>();

        while (m * n > 0) {
            for (int k = 0; k < n; k++) {
                j += dir;
                output.add(matrix[i][j]);
            }

            m--;

            for (int k = 0; k < m; k++) {
                i += dir;
                output.add(matrix[i][j]);
            }

            n--;
            dir *= -1;
        }

        return output;
    }
}
