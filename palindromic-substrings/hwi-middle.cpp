class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size();
        if (n == 0)
        {
            return 0;
        }

        vector<vector<int>> dp(n, vector<int>(n));

        int ans = n;
        for (int i = 0; i < n; ++i)
        {
            dp[i][i] = true;
        }

        for (int i = 0; i < n - 1; ++i)
        {
            dp[i][i + 1] = (s[i] == s[i + 1]);
            ans += dp[i][i + 1];
        }

        for (int l = 3; l <= n; ++l)
        {
            for (int i = 0, j = i + l - 1; j < n; ++i, ++j) 
            {
                dp[i][j] = dp[i + 1][j - 1] && (s[i] == s[j]);
                ans += dp[i][j];
            }
        }

        return ans;
    }
};
