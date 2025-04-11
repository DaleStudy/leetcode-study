#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

/*
	TC: O(n^2)
		- sort: O(nlogn)
		- 바깥루프 * 안쪽루프: O(n^2)
	SC: O(1)

	풀이 방법:
		- nums 배열을 오름차순으로 정렬
		- 첫번째 숫자를 기준으로, 나머지 두 숫자는 투 포인터로 탐색
		- 세 수의 합이 0이면 ans에 추가
		- 중복되는 값들은 건너뛰면서 ans배열에 중복되는 벡터가 들어가지 않도록 한다
*/
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
		vector<vector<int>> ans;

		sort(nums.begin(), nums.end());

		for (int idx = 0; idx < nums.size() - 2; idx++)		
		{
			// 중복되는 숫자 건너뛰기
			if (idx > 0 && nums[idx] == nums[idx - 1])
				continue ;

			int left = idx + 1;
			int right = nums.size() - 1;

			while (left < right)
			{
				int sum = nums[idx] + nums[left] + nums[right];

				if (sum < 0)
					left++;
				else if (sum > 0)
					right--;
				else
				{
					// 합이 0인 경우 벡터 ans에 삽입
					ans.push_back({nums[idx], nums[right], nums[left]});

					// 중복되는 숫자 건너뛰기
					while (left < right && nums[left] == nums[left + 1])
						left++;
					while (left < right && nums[right] == nums[right - 1])
						right--;

					left++;
					right--;
				}
			}
		}
		return (ans);
    }
};
