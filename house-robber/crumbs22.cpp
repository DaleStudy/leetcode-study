#include <iostream>
#include <vector>

using namespace std;
/*
    TC: O(n)
    SC: O(n)

    풀이 방법: 벡터 nums가 비어있을 때부터 시작해 단계적으로 nums의 마지막 요소까지 올라가며 dp 배열을 만든다.
            단 nums가 비어있으면 0을 반환하고, nums에 하나만 있다면 해당 값을 반환하며
                nums에 2개가 있을 시엔 두 값 중 큰 값을 반환한다
            dp[i]는 i번째 집까지 털었을 때 얻을 수 있는 최대 금액을 저장한다
            - 점화식 : dp[i] = max(dp[i-1], dp[i-2] + nums[i])
*/
class Solution {
public:
    int rob(vector<int>& nums) {
        vector<int> dp;
		int cnt;

        if (nums.size() == 0)
            return (0);
        if (nums.size() == 1)
            return (nums.back());
        if (nums.size() == 2)
            return (nums.front() > nums.back() ? nums.front() : nums.back());

		dp.push_back(0);
        dp.push_back(nums.front());
		for (int i = 2; i - 1 < nums.size(); i++)
		{
			dp[i - 2] + nums[i - 1] > dp[i - 1] ? \
				cnt = dp[i - 2] + nums[i - 1] : cnt = dp[i - 1];
			dp.push_back(cnt);
		}
		return (dp.back());
    }
};
