class Solution {
    public:
        int longestCommonSubsequence(string text1, string text2) {
            int t1_len = text1.length();
            int t2_len = text2.length();
            vector<vector<int>> dp(t1_len + 1, vector(t2_len + 1, 0));
    
            for(int i = 1; i <= t1_len; i++){
                for(int j = 1; j <= t2_len; j++){
                    if(text1[i-1] == text2[j-1])
                        dp[i][j] = dp[i-1][j-1] + 1;
                    else
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
    
            return dp[t1_len][t2_len];
        }
    };
