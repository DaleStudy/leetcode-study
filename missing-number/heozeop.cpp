// time complexity: O(n)
// spatial complexity: O(n)

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        set<int> exisingNums(nums.begin(), nums.end());

        int answer = -1;
        for(int i = 0; i <= nums.size(); ++i) {
            if(exisingNums.find(i) == exisingNums.end()) {
                answer = i;
                break;
            }
        }

        return answer;
    }
};
