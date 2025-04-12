#include <iostream>

/*
	TC:O(n)
	SC:O(1)

	풀이방법:
		- 점화식: f(n) = f(n-1) + f(n-2)
		- tmp: f(n-2)
		- tmp2: f(n-1)
		- tmp3: 임시 저장용
		- 반복문을 통해 f(n)까지 bottom up 방식으로 계산
*/

class Solution {
public:
    int climbStairs(int n) {
		int tmp = 1;
		int tmp2 = 2;
		int tmp3;

		if (n == 1)
			return (1);
		if (n == 2)
			return (2);
		for (int i = 2; i < n; i++)
		{
			tmp3 = tmp;
			tmp = tmp2;
			tmp2 = tmp2 + tmp3;
		}
		return (tmp2);
    }
};
