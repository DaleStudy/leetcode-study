#include <iostream>
#include <algorithm>
using namespace std;

/*
	시간 복잡도 : O(n)
	공간 복잡도 : O(1)
	
	구간 길이 windowSize = (right - left + 1)에서,
		windowSize - maxCount <= k 이면 이 구간을 모두 같은 문자로 만들 수 있다
		windowSize - maxCount > k 이면 교체가능한 횟수가 초과되었으므로 left를 한 칸 밀어서 구간을 줄인다 
*/
class Solution {
	public:
		int characterReplacement(string s, int k) {
			int left = 0;
			int maxCount = 0;
			int answer = 0;
			int count[26] = {0};
			
			for (int right = 0; right < s.size(); right++) {

				count[s[right] - 'A']++;
				maxCount = max(maxCount, count[s[right] - 'A']); // 윈도우 안에서 가장 많은 빈도를 갱신
				while (right - left + 1 - maxCount > k) {
					count[s[left] - 'A']--;
					left++;
				}
				answer = max(answer, right - left + 1);

			}
			return (answer);
		}
	};
