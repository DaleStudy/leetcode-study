class Solution {
    /**
    1. understanding
    - 3 x 3 = N x M
    - (1,2,3) -> (6,9) // (8,7) -> (4) // (5)
    - upper: step M count, N -= 1 // right: step N count, M -= 1 // bottom: step M count, N -= 1 // left: step N count, M -= 1
    2. complexity:
    - time: O(N * M)
    - space: O(1)
    */
    public List<Integer> spiralOrder(int[][] matrix) {
        int r = 0;
        int c = -1;
        int dir = 1;
        int N = matrix.length;
        int M = matrix[0].length;
        List<Integer> ret = new ArrayList<>();

        while (0 < N && 0 < M) {
            for (int i = 0; i < M; i++) {
                c += dir;
                ret.add(matrix[r][c]);
            }
            N -= 1;
            for (int i = 0; i < N; i++) {
                r += dir;
                ret.add(matrix[r][c]);
            }
            M -= 1;

            dir *= -1;
        }

        return ret;
    }
}

