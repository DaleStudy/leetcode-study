// time complexity: O(n)
// spatail complexity: O(n)

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> exisingNum(nums.begin(), nums.end());

        int maxLength = 0, length;
        for(int num : nums) {
            if(exisingNum.find(num - 1) != exisingNum.end()) {
                continue;
            }

            length = 1;
            while(exisingNum.find(num + length) != exisingNum.end()) {
                ++length;
            }

            maxLength = max(maxLength, length);
        }

        return maxLength;
    }
};
