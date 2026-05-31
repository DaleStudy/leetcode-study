// class Solution {
// public:
//     bool canJump(vector<int>& nums) {
//         int n = nums.size();
//         vector<bool> dp(n);

//         dp[n - 1] = true;
//         for(int i = n - 2; i >= 0; i--) {
//             for(int j = min(n - 1, nums[i] + i); i <= j; j--) {
//                 if(dp[j]) {
//                     dp[i] = true;
//                     break;
//                 }
//             }
//         }

//         return dp[0];
//     }
// };

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxPos = 0;
        for(int i = 0; i < nums.size(); i++) {
            if(maxPos < i)
                return false;
            maxPos = max(maxPos, i + nums[i]);
        }

        return true;
    }
};

