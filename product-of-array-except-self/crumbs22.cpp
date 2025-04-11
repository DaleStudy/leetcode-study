#include <iostream>
#include <vector>

using namespace std;

/*
	TC:O(n)
	SC:O(1)
		- 정답 배열 ans를 제외한 추가 공간 없음

	풀이 방법: 
		- 첫번째 반복문: 각 인덱스 기준 왼쪽 요소들의 누적 곱 저장
		- 두번째 반복문: 각 인덱스 기준 오른쪽 요소들의 누적 곱과 곱

*/

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans(nums.size());

		ans[0] = 1;
		for (int i = 1; i < nums.size(); i++)
			ans[i] = ans[i - 1] * nums[i - 1];

		int tmp = 1;
		for (int i = nums.size() - 1; i >= 0; i--)
		{
			ans[i] *= tmp;
			tmp *= nums[i];
		}

		return (ans);
    }
};
