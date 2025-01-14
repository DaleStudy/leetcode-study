/*
Time Complexity: O(m * n)
Space Complexity: O(1)

현재 위치를 r, c라는 변수를 사용해서 나타내고, 이 r, c를 직접 제어하는 방식으로 행렬을 순회한다.
*/
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ans = new ArrayList<>();

        int m = matrix.length, n = matrix[0].length;
        int r = 0, c = 0;
        int[] dr = {0, 1, 0, -1};
        int[] dc = {1, 0, -1, 0};
        int d = 0;
        final int VISITED = -999;

        while (ans.size() < m * n) {
            ans.add(matrix[r][c]);
            matrix[r][c] = VISITED;

            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || matrix[nr][nc] == VISITED) {
                d = (d + 1) % 4;
                nr = r + dr[d];
                nc = c + dc[d];
            }
            r = nr;
            c = nc;
        }

        return ans;
    }
}
