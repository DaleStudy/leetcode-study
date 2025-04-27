class Solution {
    public:
        bool wordBreak(string s, vector<string>& wordDict) {
            vector<bool> dp(s.length()+1, false);
    
            dp[0] = true;
    
            for(int i = 1; i <= s.length(); i++){
                for(string& word : wordDict){
                    int len = word.length();
                    if(i - len >= 0 && s.substr(i-len, len) == word)
                        dp[i] = dp[i - len];
                    
                    if(dp[i])
                        break;
                }
            }
    
            return dp[s.length()];
        }
    };
