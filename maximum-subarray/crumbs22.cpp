#include <iostream>
#include <vector>
#include <climits>

using namespace std;


/*
	TC: O(n)
	SC: O(1)
	풀이 방법:
		- sum에 현재 값을 더해가면서 최대값을 갱신한다
		- 누적합이 음수가 됐을 때 0으로 리셋한다
	
	고민했던 케이스(left와 right 포인터를 두고 풀었을 때):
		[-2, -1]
		[-1, -2]
		[-2,  1]
		[-1, 1, 2, 1]
*/
class Solution {
public:
    int maxSubArray(vector<int>& nums) {

		int max = nums[0];
		int sum = 0;

		for (int i = 0; i < nums.size(); i++)
		{
			sum += nums[i];
			if (sum > max)
				max = sum;
			if (sum < 0)
				sum = 0;
		}
		return (max);
    }
};
