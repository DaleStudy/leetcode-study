// O(n^2) 풀이
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

// O(n log n) 풀이
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> d; // d[i] = 길이가 i + 1인 LIS의 가장 작은 마지막 값

        for (int i = 0; i < n; ++i)
        {
            auto it = lower_bound(d.begin(), d.end(), nums[i]);
            if (it == d.end()) // nums[i]가 d의 모든 원소보다 큰 경우
            {
                d.push_back(nums[i]);
            }
            else // nums[i]의 자리를 찾은 경우
            {
                *it = nums[i]; // 그냥 대체하는게 이득임 -> 길이는 유지됐고, 더 이어붙일 수 있는 수의 범위는 늘어나므로
            }
        }

        return d.size();
    }
};
