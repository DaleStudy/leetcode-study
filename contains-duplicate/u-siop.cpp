class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // instinct : sort the array and check all the array whether duplicate or not
        // time complexity : NlogN(sort) + N(check all the array)
        // space complexity : 1

        // how do we, in real world, judge there is a duplicated element, definitely need a reference( another data strucrue) to check

        unordered_map<int, bool> seen; // using hash map for updating, already have seen the element

        for (const auto& i : nums) {
            if (seen[i] >= 1)
                return true;
            seen[i] = true;
        }

        return false;
    }
};