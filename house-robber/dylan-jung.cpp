// TC: O(N), SC: O(1)
class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        
        int prev2 = nums[0];        // dp[i-2]
        int prev1 = max(nums[0], nums[1]); // dp[i-1]
        
        for (int i = 2; i < nums.size(); i++) {
            int cur = max(prev1, prev2 + nums[i]); 
            prev2 = prev1;
            prev1 = cur;
        }
        
        return prev1;
    }
};
