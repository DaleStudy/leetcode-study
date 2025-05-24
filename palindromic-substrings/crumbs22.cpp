#include <iostream>

using namespace std;

/*
	중심 확장 방식
	전체 문자열길이 n에 대해서
		- 홀수 길이용 n개
		- 짝수 길이용 n - 1개
		전체 2n - 1개의 중심에서 각 양쪽으로 확장하며 카운트
*/
class Solution {
public:
    int countSubstrings(string s) {
		int answer = 0;
		int n = s.size();

		for (int center = 0; center < 2 * n - 1; center++) {
			int left = center / 2;
			int right = left + (center % 2);

			while (left >= 0 && right < n && s[left] == s[right]) {
				answer++;
				left--;
				right++;
			}
		}
		return (answer);
	}
};
