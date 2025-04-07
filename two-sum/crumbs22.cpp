#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/*
	TC: O(n^2)
		- 외부 루프: 벡터 nums의 모든 요소를 순회 (O(n))
		- 내부 루프: 현재 요소 이후의 모든 요소를 탐색하여 complement와 일치하는 값을 찾음 (O(n))
		=> 전체 시간 복잡도는 O(n^2)

	SC: O(1)

	풀이 방법: 각 요소에 대해 타겟에서 해당 요소를 뺀 값을(complement) 계산하고, 나머지 요소들 중에서 해당 값을 탐색한다.
*/
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
		int complement;
		if (nums.size() == 2)
			return {1, 2};

		for (int i = 0; i < nums.size(); i++)
		{
			complement = target - nums[i];
			for (int j = i + 1; j < nums.size(); j++)
			{
				if (nums[j] == complement)
				{
					return {i, j};
				}
			}
		}
		return {-1};
    }
};
