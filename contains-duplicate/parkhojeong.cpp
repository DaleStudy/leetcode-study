// Time Complexity: O(n) on average
// Space Complexity: O(n)

#include <unordered_set>

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for(int n: nums) {
            if(seen.count(n)) return true;
            seen.insert(n);
        }

        return false;
    }
};
