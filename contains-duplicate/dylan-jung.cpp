class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> s;
        for(auto item: nums) {
            if(s.count(item) > 0) return true;
            s.insert(item);
        }
        return false;
    }
};
