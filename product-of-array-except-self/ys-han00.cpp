class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int mul = 1, zero_cnt = 0;

        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] != 0)
                mul *= nums[i];
            else
                zero_cnt++;
        }

        vector<int> ans = vector<int>(nums.size(), 0);
                
        if(zero_cnt == 1) {
            for(int i = 0; i < nums.size(); i++) {
                if(nums[i] == 0) {
                    ans[i] = mul;
                    break;
                }
            }
        } else if(zero_cnt == 0) {
            for(int i = 0; i < nums.size(); i++)
                ans[i] = mul / nums[i];
        }

        return ans;
    }
};

