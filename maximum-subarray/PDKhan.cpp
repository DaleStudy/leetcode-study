class Solution {
    public:
        int maxSubArray(vector<int>& nums) {
            int cur = nums[0];
            int max = nums[0];
    
            for(int i = 1; i < nums.size(); i++){
                if(nums[i] > cur + nums[i])
                    cur = nums[i];
                else
                    cur = cur + nums[i];
                
                if(max < cur)
                    max = cur;
            }
    
            return max;
        }
    };
