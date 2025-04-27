#include <iostream>
#include <vector>

using namespace std;

/*
	O(logn)으로 풀어라
		- 이진 탐색 느낌
		- mid값과 오른쪽 끝을 비교,
			- mid > 오른쪽 끝 : 최소는 오른쪽에
			- mid <= 오른쪽 끝 : 최소는 mid 포함 왼쪽에
*/

class Solution {
	public:
		int findMin(vector<int>& nums) {
			int left = 0;
			int right = nums.size() - 1;

			while (left < right) {
				int mid =  left + (right - left) / 2;

				if (nums[mid] > nums[right]) {
					left = mid + 1;
				}
				else {
					right = mid;
				}
			}
			return (nums[left]);
		}
	};
