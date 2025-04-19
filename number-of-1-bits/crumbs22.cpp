#include <iostream>

using namespace std;

/*
	TC: O(1)
	SC: O(1)
	풀이방법:
		- n의 비트를 오른쪽으로 이동시키면서 최하위 비트가 1인지 확인한다
		- n이 int형이므로 cnt는 32를 넘을 수 없다
*/

class Solution {
public:
    int hammingWeight(int n) {
		int cnt = 0;

		while (n && cnt <= 31)
		{
			if (n & 1)
				cnt++;
			n >>= 1;
		}
		return (cnt);
    }
};
