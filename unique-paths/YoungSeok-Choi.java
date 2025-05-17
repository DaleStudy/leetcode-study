// NOTE: 2 * X 부터 모든 경우를 세어보니, 3 * 3의 격자가 나왔을 때 2 * 3, 3 * 2 경우를 더한 값이 나오는 것을 알 수 있었음
// +)  3 * 4 격자에 대한 답은 3 * 3 격자의 답 + 2 * 4 격자의 답을 더하면 만들어지는 것을 알수 있었고, 아래와 같은 점화식을 만들 수 있었음
// memo[m][n] = memo[m][n - 1] + memo[m - 1][n]
class Solution {
  public int uniquePaths(int m, int n) {
    int[][] memo = new int[101][101];

    if (m == 1 || n == 1) {
      return 1;
    }

    memo[2][2] = 2;
    for (int i = 2; i < 3; i++) {
      for (int j = 3; j < 101; j++) {
        memo[i][j] = j;
        memo[j][i] = j;
      }
    }

    for (int i = 3; i < 101; i++) {
      memo[i][i] = memo[i][i - 1] + memo[i - 1][i];
      for (int j = i + 1; j < 101; j++) {
        int val = memo[i][j - 1] + memo[i - 1][j];
        memo[i][j] = val;
        memo[j][i] = val;
      }
    }

    return memo[m][n];
  }
}
