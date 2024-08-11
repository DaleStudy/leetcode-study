class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> unique;
        for (int i : nums) {
            if (unique.find(i) != unique.end()) {
                return true;
            }
            unique.insert(i);
        }
        return false;
    }
};
