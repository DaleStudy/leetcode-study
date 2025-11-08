class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> s;

        for(const auto& n : nums) {
            auto iter = s.find(n);
            if(iter != s.end()){
                return true;
            }
            s.insert(n);
        }
        return false;
    }
};