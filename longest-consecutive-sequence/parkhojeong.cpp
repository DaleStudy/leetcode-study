// Time Complexity: O(n) on average
// Space Complexity: O(n)

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int N = nums.size();
        unordered_set<int> s(nums.begin(), nums.end());
        int best = 0;
        for(int x: s) {
            if(s.count(x - 1)) continue;

            int len = 1;
            while(s.count(x + len)) len++;
            best = max(best, len);
        }

        return best;
    }
};
