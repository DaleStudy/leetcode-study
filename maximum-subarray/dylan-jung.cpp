class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int dp[100000];
        dp[0] = max(nums[0], -(1<<30));
        for(int i = 1; i < nums.size(); i++) {
            dp[i] = max(dp[i-1] + nums[i], nums[i]);
        }
        int m = dp[0];
        for(int i = 1; i < nums.size(); i++) {
            m = max(dp[i], m);
        }
        return m;
    }
};
