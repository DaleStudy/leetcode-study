#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
		if (nums.size() == 2)
			return {1, 2};
		int tmp;
		for (int i = 0; i < nums.size(); i++)
		{
			tmp = target - nums[i];
			for (int j = i + 1; j < nums.size(); j++)
			{
				if (nums[j] == tmp)
				{
					return {i, j};
				}
			}
		}
		return {-1};
    }
};
