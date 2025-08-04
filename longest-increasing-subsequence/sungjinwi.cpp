/*
    nums와 길이가 같은 dp배열을 만들고 1로 초기화한다
    dp[i]의 값은 nums[i]으로 끝나는 LIS의 길이
    i 이후의 j에 대해 nums[j] > nums[i]일 경우 nums[j]를 nums[i]로 끝나는 LIS에 붙일 수 있으므로
    dp[j]와 dp[i + 1]을 비교해 큰 값으로 업데이트

    nums의 길이 : N

    TC : O(N^2)
        반복문 내부의 반복문

    SC : O(N)
        dp의 길이는 nums길이에 비례
*/

class Solution {
    public:
        int lengthOfLIS(vector<int>& nums) {
            vector<int> dp(nums.size(), 1);
            int max_len = 1;
    
            for (int i = 0; i < nums.size(); i++)
                for (int j = i + 1; j < nums.size(); j++)
                {
                    if (nums[j] > nums[i])
                    {
                        dp[j] = max(dp[i] + 1, dp[j]);
                        max_len = max(dp[j], max_len);
                    }
                }
            return max_len;
        }
    };
