// Time Complexity : O(n)
// Spatial Complexity : O(n)

#include <set>

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> count;

        for(int num : nums) {
            if (count.find(num) != count.end()) {
                return true;
            }
            count.insert(num);
        }

        return false;
    }
};
