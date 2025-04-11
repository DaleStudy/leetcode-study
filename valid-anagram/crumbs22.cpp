#include <iostream>
#include <string>

using namespace std;

/*
	TC:O(n)
	SC:O(1)

	풀이방법:
		- ascii 기준으로 문자 빈도를 저장할 cnt 배열 선언
		- s의 각 문자 등장 횟수를 cnt에 +1
		- t의 각 문자는 cnt에서 -1
		- cnt 배열의 모든 값이 0이면 두 문자열은 아나그램이다
*/

class Solution {
public:
    bool isAnagram(string s, string t) {
		char	cnt[256];

		// cnt 배열 0으로 초기화
		for (char &value : cnt)
			value = 0;
		
		for (char ch : s)
			cnt[ch]++;
		
		for (char ch : t)
			cnt[ch]--;
		
		for (int i = 0; i < 256; i++)
		{
			if (cnt[i] != 0)
				return (false);
		}
		return (true);
    }
};
