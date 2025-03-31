class Solution {
    public:
        int rob(vector<int>& nums) {
            vector<int> dp;
    
            for(int i = 0; i < nums.size() + 3; i++){
                dp.push_back(0);
            }
    
            for(int i = nums.size()-1; i >= 0; i--){
                if(dp[i+2] + nums[i] > dp[i+3] + nums[i])
                    dp[i] = dp[i+2] + nums[i];
                else
                    dp[i] = dp[i+3] + nums[i];
            }
    
            if(dp[0] > dp[1])
                return dp[0];
            else
                return dp[1];
        }
    };
