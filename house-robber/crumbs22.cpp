#include <iostream>
#include <vector>
using namespace std;

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
