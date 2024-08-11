/**
 * for given size of input nums N,
 * 
 * Time complexity: O(N)
 *   - iteration: O(N)
 *   - unorderd_set find method: O(1) on average
 *   - unorderd_set insert method: O(1) on average
 * 
 * Space complexity: O(N)
 */

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> us;

        auto it = nums.begin();
        while (it != nums.end()) {
            if (us.find(*it) == us.end()) us.insert(*(it++));
            else return true;
        }
        return false;
    }
};