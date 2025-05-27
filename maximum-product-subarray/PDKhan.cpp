class Solution {
    public:
        int maxProduct(vector<int>& nums) {
            int result = nums[0];
            int curr_max = nums[0];
            int curr_min = nums[0];
    
            for(int i = 1; i < nums.size(); i++){
                int tmp_max = curr_max;
    
                curr_max = max(nums[i], max(curr_max * nums[i], curr_min * nums[i]));
                curr_min = min(nums[i], min(tmp_max * nums[i], curr_min * nums[i]));
    
                result = max(result, curr_max);
            }
    
            return result;
        }
    };
