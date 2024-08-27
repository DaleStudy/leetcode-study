class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> past; // key: num value: index
        vector<int> res;

        past.insert({nums[0], 0});

        for (int i = 1; i < nums.size(); i++) {
            int remainder = target - nums[i];

            if (past.find(remainder) != past.end()) {
                res.push_back(i);
                res.push_back(past[remainder]);
                break;
            } else {
                past.insert({nums[i], i});
            }
        }

        return res;
    }
};
