/*
input : string s
output: the number of palindromic substrings of given string
tc : O(n^2) sc : o(n^2) when n is the length of string s

optimize?
maybe nope.. atleast n^2 to select i and j

 */
class Solution {
  public int countSubstrings(String s) {
    int n = s.length();
    int cnt = 0;
    boolean[][] dp = new boolean[n][n];
    for(int i = n-1; i >= 0; i--) {
      for(int j = i; j < n; j++) {
        dp[i][j] = s.charAt(i) == s.charAt(j) && (j-i +1 < 3 || dp[i+1][j-1]);
        if(dp[i][j]) cnt++;
      }
    }
    return cnt;
  }
}
// Compare this snippet from valid-palindrome-ii/ekgns33.java: