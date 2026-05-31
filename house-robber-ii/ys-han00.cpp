class Solution {
public:
    int rob(vector<int>& nums) {
        vector<vector<int>> dp(2, vector<int>(nums.size(), 0));

        dp[0][0] = nums[0];
        if(nums.size() == 1) 
            return dp[0][0];
        
        dp[0][1] = nums[1];
        dp[1][1] = nums[1];
        
        int ans = max(dp[0][0], dp[0][1]);
        for(int i = 2; i < nums.size(); i++) {
            int maxi = -1, maxi2 = -1;
            for(int j = 0; j < i - 1; j++) {
                maxi = max(dp[0][j], maxi);
                maxi2 = max(dp[1][j], maxi2);
            }

            dp[0][i] = maxi + nums[i];
            dp[1][i] = maxi2 + nums[i];
            
            if(i != nums.size() - 1)
                ans = max(ans, dp[0][i]);
            ans = max(ans, dp[1][i]);
        }
        return ans;
    }
};

