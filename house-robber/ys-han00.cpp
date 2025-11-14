class Solution {
public:
    int rob(vector<int>& nums) {
        vector<int> dp(nums.size(), 0);

        dp[0] = nums[0];
        if(dp.size() == 1) 
            return dp[0];
        
        dp[1] = nums[1];
        int ans = max(dp[0], dp[1]);
        
        for(int i = 2; i < dp.size(); i++) {
            int maxi = -1;
            for(int j = 0; j < i - 1; j++)
                maxi = max(dp[j], maxi);
            dp[i] = maxi + nums[i];
            ans = max(ans, dp[i]);
        }

        return ans;
    }
};

