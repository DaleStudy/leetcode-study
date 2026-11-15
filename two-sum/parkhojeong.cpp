// Time Complexity: O(n) on average
// Space Complexity: O(n)

#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> index_of;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            if (index_of.count(complement)) {
                return {index_of[complement], i};
            }
            index_of[nums[i]] = i;
        }
        return {};
    }
};
