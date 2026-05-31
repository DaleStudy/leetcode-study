class Solution {
public:
    string longestPalindrome(string s) {
        int max_s = 0, max_e = 0;
        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        
        for(int i = n - 1; i >= 0; i--) {
            for(int j = i; j < n; j++) {
                if(i == j)
                    dp[i][j] = true;
                else if(i + 1 == j)
                    dp[i][j] = (s[i] == s[j]);
                else
                    dp[i][j] = (s[i] == s[j]) && dp[i + 1][j - 1];

                if(dp[i][j] && max_e - max_s < j - i) {
                    max_s = i;
                    max_e = j;
                }
            }
        }

        return s.substr(max_s, max_e - max_s + 1);
    }
};
