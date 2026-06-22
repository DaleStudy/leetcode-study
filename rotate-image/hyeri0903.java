class Solution {
    public void rotate(int[][] matrix) {
        /**
        1.90도 시계방향으로 회전한 matrix return
        2.constraints : in-place 로 rotate 할 것
        3.solution: 2단계 처리
        1) 대각선 기준 뒤집기 transpose, matrix[i][j] => matrix[j][i]
        2) 각 행 reverse
        time complexity : O(n^2), space: O(1)
         */

         int n = matrix.length;

         //1.transpose
         for(int i = 0; i < n; i++) {
            for(int j = i+1; j < n; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
         }

         //2.reverse each row
         for(int i = 0; i < n; i++) {
            reverse(matrix[i]);
         }
    }

    void reverse(int[] row) {
        int left = 0;
        int right = row.length - 1;

        while(left < right) {
            int tmp = row[left];
            row[left] = row[right];
            row[right] = tmp;

            left++;
            right--;
        }
    }
}
