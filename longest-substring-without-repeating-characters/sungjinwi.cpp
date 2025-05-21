/*
    풀이 :
        슬라이딩 윈도우 기법을 사용해서 풀이
        right가 현재까지 문자열에 포함되지 않는 문자면 right의 문자를 set에 추가 후 right 증가, 문자열길이를 늘리고 최대길이와 비교해서 업데이트
        이미 문자열에 포함되는 문자면 left의 문자를 set에서 제거 후 left 증가

    문자열 길이 : N
    
    TC : O(N)
        문자열 전체에 대해 1회 순회
    
    SC : O(N)
        해시테이블 unordered_set의 크기는 문자열 길이에 비례

    추가적인 최적화 방법 :
        int lastIdx[256] 선언하고 아스키코드 위치에 마지막으로 해당 문자가 나온 인덱스를 저장한다
        ex) a가 10번쨰 인덱스에서 나오면 lastIdx['a'] = 10;
        나중에 중복되는 문자를 만나는 경우 left를 1씩 전진시키는 것이 아니라 중복된 문자의 마지막 바로 다음으로 left를 업데이트
*/

#include <unordered_set>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0;
        int left = 0, right = 0;
        unordered_set<char> lookup;

        while (right < s.size())
        {
            if (lookup.find(s[right]) == lookup.end()) {
                ans = max(ans, right - left + 1);
                lookup.insert(s[right]);
                right++;
            }
            else {
                lookup.erase(s[left]);
                left++;
            }
        }

        return ans;
    }
};
