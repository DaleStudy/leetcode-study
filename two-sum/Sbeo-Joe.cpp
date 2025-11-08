class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        for(int i = 0; i < nums.size() - 1; i++){
            for(int j = i + 1; j < nums.size(); j++){
                if(nums[i] + nums[j] == target){
                    return std::vector<int>{i, j};
                }
            }
        }
        return {};
    }
};

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // value, index;
        unordered_map<int, int> um;
        for(int i = 0; i < nums.size(); i++){
            int gap = target - nums[i]; 
            if(um.count(gap)){
                return {um[gap], i};
            }
            um[nums[i]] = i;
        }
        return {};
    }
};