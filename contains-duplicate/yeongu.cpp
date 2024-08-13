// Time complexity: o(n log n) 왜냐하면, for 문이 n이고 find 연산이 log n이기 때문.
// Space complexity: O(n) 왜냐하면, 다 다른경우 n

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
