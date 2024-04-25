// https://leetcode.com/problems/contains-duplicate/
// Time Complexity : O(n)
// Space Complexity : O(n)

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, bool> hm;
        for(int x : nums) {
            if(hm[x]) return true;
            hm[x] = true;
        }
        return false;        
    }
};
