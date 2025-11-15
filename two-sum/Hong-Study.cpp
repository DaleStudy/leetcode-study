class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int, int> numMap;
        for (int i = 0; i < nums.size(); i++) {
            int leftNum = target - nums[i];
            if (numMap.find(leftNum) == numMap.end()) {
                numMap[nums[i]] = i;
                continue;
            }

            int idx = numMap[leftNum];
            return std::vector<int>{idx, i};
        }

        return std::vector<int>{0, 0};
    }
};

