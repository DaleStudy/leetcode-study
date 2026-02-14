class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> dp(n + 1, 0);
        for(int i = 1; i <= n; i++)
            dp[i] = dp[(i >> 1)] + (i & 1);

        return dp;
    }

    // vector<int> countBits(int n) {
    //     vector<int> dp(n + 1, 0);
    //     int msb = 1;

    //     for(int i = 1; i <= n; i++) {
    //         if(msb << 1 == i)
    //             msb <<= 1;
    //         dp[i] = 1 + dp[i - msb];
    //     }
    //     return dp;   
    // }

    // vector<int> countBits(int n) {
    //     vector<int> dp(n + 1, 0);
    //     dp[0] = 0;
    //     if(n >= 1)
    //         dp[1] = 1;
    //     for(int i = 2; i <= n; i *= 2) {
    //         for(int j = 0; j < i; j++) {
    //             if(i + j > n)
    //                 break;
    //             dp[i + j] = dp[i / 2 + j];
    //             if(j >= i / 2) dp[i + j]++;
    //         }
    //     }

    //     return dp;
    // }
};

