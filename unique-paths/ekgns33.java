/*
input : 2D matrix 
output : the number of possible unique paths
constraints : 
1) range of m and n
[1, 100]

solution 1) dfs?
move right or move down.
tc : O(mn)
sc : O(mn)

solution 2) dp + tabulation
let dp[i][j] the number of unique paths from starting point.
    there are only 2 way to get coordinate i, j 
        1) from i-1, j
        2) from i, j-1
dp[i][j] = dp[i-1][j] + dp[i][j-1]

tc : O(mn)
sc : O(mn)
 */

class Solution {
  public int uniquePaths(int m, int n) {
    int[][] dp = new int[m][n];
    for(int i = 0; i < m; i++) {
      for(int j = 0; j < n; j++) {
        if(i == 0 || j == 0) {
          dp[i][j] = 1;
          continue;
        }
        dp[i][j] = dp[i][j-1] + dp[i-1][j];
      }
    }
    return dp[m-1][n-1];
  }
}
