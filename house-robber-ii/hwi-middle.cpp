class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1)
        {
            return nums[0];
        }
        
        // 1번째 집과 n번째 집이 이웃하므로, [1, n)과 (1, n]에 대해 탐색 후 최댓값 반환
        return max(sol(span(nums).subspan(0, nums.size() - 1)), sol(span(nums).subspan(1)));
    }

    int sol(span<int> nums) {
        int len = nums.size() + 1;
        vector<int> d(len);
        d[0] = 0;
        d[1] = nums[0];
        for(int i = 2; i < len; ++i)
        {
            d[i] = max(d[i - 1], d[i - 2] + nums[i - 1]);
        }

        return d[len - 1];
    }
};
