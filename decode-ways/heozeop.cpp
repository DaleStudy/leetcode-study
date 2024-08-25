// Time Complexity: O(n)
// Spatial Complexity: O(n)

class Solution {
public:
  int numDecodings(string s) {
    if(s.length() < 1 || s[0] == '0') {
      return 0;
    }

    vector<int> dp(s.length() + 1, 0);
    dp[0] = dp[1] = 1;
    if(s[1] == '0') {
      dp[1] = 0;
    }

    int prev,pprev;
    for(int i = 2; i <= s.length(); ++i) {
      prev = s[i - 1] - '0';
      if (prev <= 9 && prev > 0) {
        dp[i] += dp[i-1];
      }
      pprev = (s[i - 2] - '0') * 10 + prev;
      if(pprev <= 26 && pprev > 9) {
        dp[i] += dp[i-2];
      }
    }

    return dp[s.length()];
  }
};
