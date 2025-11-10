class Solution {
public:
    int dp[100] = { 0 };
    int rob(vector<int>& nums) {
        dp[0] = nums[0];
        if(nums.size() >= 2) {
            dp[1] = nums[1];
        }
        for(int i = 2; i < nums.size(); i++) {
            for(int j = 0; j < i-1; j++) {
                dp[i] = max(dp[j] + nums[i], dp[i]);
            }
        }
        int m = -1;
        for(int i = 0; i < nums.size(); i++) {
            m = max(dp[i], m);
        }
        return m;
    }
};
