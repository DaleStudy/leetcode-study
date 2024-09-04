// Time complexity: O(n)
// Spatial complexity: O(n)

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int numberOfZero = 0, productNums = 1;

        for (int num : nums) {
            if(num == 0) {
                ++numberOfZero;
                continue;
            }

            productNums *= num;
        }

        vector<int> answer(nums.size(), 0);
        if (numberOfZero > 1) {
            return answer;
        }

        if (numberOfZero == 1) {
            for(int i = 0; i < nums.size(); ++i) {
                if(nums[i] == 0) {
                    answer[i] = productNums;
                    return answer;
                }
            }
        }

        for(int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 0) {
                answer[i] = productNums;
                continue;
            }

            answer[i] = productNums / nums[i];
        }

        return answer;
    }
};
