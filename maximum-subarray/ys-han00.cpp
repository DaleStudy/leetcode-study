// class Solution {
// public:
//     int maxSubArray(vector<int>& nums) {
//         vector<int> dp(nums.size(), 0x8000000);
//         int ans = 0x80000000;

//         dp[0] = nums[0];
//         ans = max(ans, dp[0]);

//         for(int i = 1; i < nums.size(); i++) {
//             dp[i] = max(dp[i - 1] + nums[i], nums[i]);
//             ans = max(ans, dp[i]);
//         }

//         return ans;
//     }
// };

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ans = 0x80000000, sum;

        sum = nums[0];
        ans = sum;
        for(int i = 1; i < nums.size(); i++) {
            sum = max(sum + nums[i], nums[i]);
            ans = max(ans, sum);
        }

        return ans;
    }
};

