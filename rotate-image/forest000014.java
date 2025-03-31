/* 
# Time Complexity: O(n^2)
# Space Complexity: O(1)
*/
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;

        for (int i = 0; i < n / 2; i++) {
            for (int j = i; j < n - i - 1; j++) {
                // [i][j] -> [j][n - i - 1]
                // [j][n - i - 1] -> [n - i - 1][n - j - 1]
                // [n - i - 1][n - j - 1] -> [n - j - 1][i]
                // [n - j - 1][i] -> [i][j]
                // (각 인덱스의 등장 횟수를 체크해서, 각각의 등장횟수가 4번임을 확인하면, 틀린 인덱스가 아님을 quick하게 체크해볼 수는 있음. 이 방법으로 맞다는 보장은 안 됨.)

                int tmp = matrix[i][j];
                matrix[i][j] = matrix[n - j - 1][i];
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1];
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1];
                matrix[j][n - i - 1] = tmp;
            }
        }
    }
}
