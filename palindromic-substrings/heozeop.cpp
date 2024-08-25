// Time Complexity: O(n^3)
// Spatial Complexity: O(1)

// #include <set>
// #include <string>

class Solution {
private:
    bool isPalindrom(string s) {
        int sLength = s.length();
        
        for(int i = 0; i < sLength / 2; ++i) {
            if(s[i] != s[sLength - 1 - i]) {
                return false;
            }
        }

        return true;
    }

public:
    int countSubstrings(string s) {
        int answer = 0;

        int sLength = s.length();
        string temp;
        for(int i = 1; i <= sLength; ++i) {
            for(int j = 0; j + i <= sLength; ++j) {
                temp = s.substr(j, i);

                if(this->isPalindrom(temp)) {
                    ++answer;
                }
            }
        }

        return answer;
    }
};

// DP version
// O(n^2)
// #include <set>
// #include <vector>

class Solution2 {
public:
    int countSubstrings(string str) {
        int answer = 0;

        int n = str.length();
        vector<vector<bool>> dp(n + 1, vector<bool>(n + 1, false));

        for(int e = 0; e < n; ++e) {
            for(int s = 0; s <= e; ++s) {
                if (str[s] != str[e]) {
                    continue;
                }

                if (s != e && s + 1 != e && !dp[s + 1][e - 1]) {
                    continue;
                }

                ++answer;
                dp[s][e] = true;
            }
        }

        return answer;
    }
};
