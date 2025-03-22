// You have to rotate the image in-place 라는말을 별 생각 안하고 풀다가 오래걸림
// "matrix내"에서 문제의 요구사항 대로 회전시켜줘야 한다. 유지해야한다
// matrix[i][j]를 matrix[j][i]로 바꾸고 각 행을 좌우로 뒤집는다.
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n / 2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][n - 1 - j];
                matrix[i][n - 1 - j] = temp;
            }
        }
    }
}
