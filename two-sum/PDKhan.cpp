class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            unordered_map<int, int> Map;
    
            for(int i = 0; i < nums.size(); i++){
                int diff = target - nums[i];
    
                if(Map.find(diff) != Map.end()){
                    return { Map[diff], i };
                }
    
                Map[nums[i]] = i;
            }
    
            return {};
        }
    };
