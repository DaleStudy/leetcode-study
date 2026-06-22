class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return nums.end() != unique(nums.begin(), nums.end());
    }
};
