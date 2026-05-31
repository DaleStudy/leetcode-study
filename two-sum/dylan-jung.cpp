// TC: O(N), SC: O(N)

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        for(int i = 0; i < nums.size(); i++) {
            m[nums[i]] = i;
        }
        for(int first = 0; first < nums.size(); first++) {
            if(m.count(target - nums[first]) > 0 && first != m[target - nums[first]]) {
                return {first, m[target - nums[first]]};
            }
        }
        return {};
    }
};
