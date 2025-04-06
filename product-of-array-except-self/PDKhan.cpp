class Solution {
    public:
        vector<int> productExceptSelf(vector<int>& nums) {
            int zero = 0;
            int product = 1;
            vector<int> result;
    
            for(int i = 0; i < nums.size(); i++){
                if(nums[i] == 0)
                    zero++;
                else
                    product *= nums[i];
            }
    
            for(int i = 0; i < nums.size(); i++){
                if(zero > 1)
                    result.push_back(0);
                else if(zero == 1){
                    if(nums[i] == 0)
                        result.push_back(product);
                    else
                        result.push_back(0);
                }else
                    result.push_back(product / nums[i]);
            }
    
            return result;
        }
    };
