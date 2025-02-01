/**
 input : string text1, text2
 output : length of lcs else 0
 constraints:
 1) both input strings are not empty
 2) input strings are consist of lowercase eng. letters

 solution 1) brute force

 nested for loop
 tc : O(n^2 * m) where n is min (len(text1), len(text2)), m is max
 sc : O(1)

 solution 2) dp

 at each step we have 3 conditions

 1. current characters are same. compare next characters
 abcde. ith index
 ^
 abc.  jth index
 ^
 then go to next and maximum length also increases
 move (i + 1, j+1)
 2, 3. current characters are different. move i or j to compare

 abcde
 ^
 abc
 ^
 move (i +1, j) or (i, j+1)


 let dp[i][j] max length of lcs

 a b c d e
 a 1 1 1 1 1
 c 1 1 2 2 2
 e 1 1 2 2 3

 a b d e f g h
 a 1 1 1 1 1 1 1
 f 1 1 1 1 2 2 2
 h 1 1 1 1 2 2 3
 d 1 1 2 2 2 2 3

 if equals
 dp[i][j] = dp[i-1][j-1] + 1
 else
 dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
 tc : O(mn)
 sc : O(mn) > O(min(m, n)) if optimize space to 2-Row array
 */
class Solution {
  public int longestCommonSubsequence(String text1, String text2) {
    int m = text1.length(), n = text2.length();
    if(m < n) {
      return longestCommonSubsequence(text2, text1);
    }
    int[][] dp = new int[2][n+1];
    int prevRow = 0;
    int curRow = 1;
    for(int i = 1; i <= m; i++) {
      for(int j = 1; j <= n; j++) {
        if(text1.charAt(i-1) == text2.charAt(j-1)) {
          dp[curRow][j] = dp[prevRow][j-1] + 1;
        } else {
          dp[curRow][j] = Math.max(dp[prevRow][j], dp[curRow][j-1]);
        }
      }
      curRow = prevRow;
      prevRow = (prevRow + 1) % 2;
    }
    return dp[prevRow][n];
  }
}
