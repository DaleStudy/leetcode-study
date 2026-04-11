class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> d(n); // 점화식: d[i] = a[i]를 마지막으로 하는 LIS 길이

        for (int i = 0; i < n; ++i)
        {
            d[i] = 1; // 최솟값은 1
            for (int j = 0; j < i; ++j)
            {
                // 증가하는 부분수열이고, 기존에 구한 길이보다 길면 업데이트
                if (nums[j] < nums[i] && d[j] + 1 > d[i])
                {
                    d[i] = d[j] + 1;
                }
            }
        }

        // d의 최댓값 반환
        return *max_element(d.begin(), d.end());
    }
};
