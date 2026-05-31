// class Solution {
// public:
//     vector<int> productExceptSelf(vector<int>& nums) {
//         int mul = 1, zero_cnt = 0;

//         for(int i = 0; i < nums.size(); i++) {
//             if(nums[i] != 0)
//                 mul *= nums[i];
//             else
//                 zero_cnt++;
//         }

//         vector<int> ans = vector<int>(nums.size(), 0);
                
//         if(zero_cnt == 1) {
//             for(int i = 0; i < nums.size(); i++) {
//                 if(nums[i] == 0) {
//                     ans[i] = mul;
//                     break;
//                 }
//             }
//         } else if(zero_cnt == 0) {
//             for(int i = 0; i < nums.size(); i++)
//                 ans[i] = mul / nums[i];
//         }

//         return ans;
//     }
// };

// class Solution {
// public:
//     vector<int> productExceptSelf(vector<int>& nums) {
//         int mul = 1, zero_cnt = 0;
//         vector<int> prefix(nums.size(), 0), postfix(nums.size(), 0);

//         prefix[0] = 1;
//         for(int i = 1; i < nums.size(); i++)
//             prefix[i] = nums[i - 1] * prefix[i - 1];

//         postfix[nums.size() - 1] = 1;
//         for(int i = nums.size() - 2; i >= 0; i--)
//             postfix[i] = nums[i + 1] * postfix[i + 1];

//         vector<int> ans = vector<int>(nums.size(), 0);
//         for(int i = 0; i < nums.size(); i++)
//             ans[i] = postfix[i] * prefix[i];

//         return ans;
//     }
// };

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans(nums.size(), 1);
        int before = 1, after = 1;

        for(int i = 0; i < nums.size() - 1; i++) {
            before *= nums[i];
            ans[i + 1] *= before;
        }

        for(int i = nums.size() - 1; i > 0; i--) {
            after *= nums[i];
            ans[i - 1] *= after;
        }

        return ans;
    }
};

