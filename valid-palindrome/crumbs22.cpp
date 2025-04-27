#include <iostream>
#include <string>
#include <cctype>

using namespace std;

/*
	TC: O(n)
		start, end 포인터가 각각 한 번씩 전체 문자열을 스캔하기 때문에
		모든 문자를 최대 한 번씩만 검사한다
	SC: O(1)
	풀이방법:
		- 양 쪽에서 포인터가 이동하면서 두 포인터가 만날 때까지 반복하며 두 문자가 일치하는지 확인한다
	고민했던 케이스:
		- 0P
*/

class Solution {
public:
    bool isPalindrome(string s) {
        int start = 0;
		int end = s.size() - 1;

		while (start < end)
		{
			// ascii 문자가 아닌 구간 건너뛰기
			while (start < end && !isalnum(s[start]))
				start++;
			while (start < end && !isalnum(s[end]))
				end--;

			if (tolower(s[start]) != tolower(s[end]))
				return (false);
			start++;
			end--;
		}
		return (true);
    }
};
