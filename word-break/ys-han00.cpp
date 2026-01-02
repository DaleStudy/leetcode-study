// class Solution {
// public:
//     bool ans = false;
//     unordered_map<int, bool> check;
//     void dfs(string s, vector<string>& wordDict, int idx) {
//         if(ans) return;
//         if(idx == s.size()) {
//             ans = true;
//             return;
//         }
//         for(auto word : wordDict) {

//             if(!check[idx + word.size()] && idx + word.size() <= s.size() && s.substr(idx, word.size()) == word) {
//                 check[idx + word.size()] = true;
//                 dfs(s, wordDict, idx + word.size());
//             }
//         }
//     }
    
//     bool wordBreak(string s, vector<string>& wordDict) {
//         dfs(s, wordDict, 0);
//         return ans;
//     }
// };

// class Solution {
// public:
//     bool dfs(const string &s, const vector<string> &wordDict, int idx, vector<int> &check) {
//         if(idx == s.size()) return true;
//         if(check[idx] != -1) return check[idx];

//         for(const auto &word : wordDict) {
//             int nextIdx = idx + word.size();
//             if(nextIdx > s.size()) continue;

//             bool matched = true;
//             for(int i = 0; i < word.size(); i++) {
//                 if(s[idx + i] != word[i]) {
//                     matched = false;
//                     break;
//                 }
//             }
//             if(!matched) continue;

//             if(dfs(s, wordDict, nextIdx, check))
//                 return check[idx] = 1;
//         }
//         return check[idx] = 0;
//     }

//     bool wordBreak(string s, vector<string>& wordDict) {
//         vector<int> check(s.size() + 1, -1);
//         return dfs(s, wordDict, 0, check);
//     }
// };

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.size(), m;
        vector<bool> dp(n + 1, false);
        dp[0] = 1;

        for(int i = 1; i <= n; i++) {
            for(string word : wordDict) {
                m = word.size();
                if(i - m < 0) continue;
                if(s.substr(i - m, m) == word)
                    dp[i] = dp[i - m];
                if(dp[i] == true)
                    break;
            }
        }

        return dp[n];
    }
};

