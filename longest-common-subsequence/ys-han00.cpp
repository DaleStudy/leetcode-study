class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int n = text1.size(), m = text2.size();
        vector<vector<int>> dp(n, vector<int> (m, 0));

        for(int i = 0; i < n ; i++) {
            for(int j = 0; j < m; j++) {
                dp[i][j] = max((i == 0 ? 0 : dp[i - 1][j]), (j == 0 ? 0 : dp[i][j - 1]));
                if(text1[i] == text2[j])
                    dp[i][j] = (i == 0 || j == 0 ? 0 : dp[i - 1][j - 1]) + 1;
            }
        }
        
        return dp[n - 1][m - 1];
    }
};

