/**
 * 풀이
 * - 주어진 문자열 `s`를 한 번 조회합니다
 * - lookup이라는 해시맵 객체를 이용하여 현재 조회하고 있는
 *   substring에 반복되는 문자가 있는지 검사합니다
 * 
 * Big O
 * - N: 주어진 문자열 `s`의 길이
 * 
 * - Time complexity: O(N)
 * - Space complexity: O(N)
 */

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() == 0) return 0;

        unordered_map<char, int> lookup;
        lookup.insert({s[0], 0});

        int res = 1;

        int start = 0;
        int end = 1;
        
        while (end < s.size()) {
            if (lookup.find(s[end]) != lookup.end()
                && lookup[s[end]] >= start) {
                start = lookup[s[end]] + 1;
            }

            lookup[s[end]] = end;

            res = max(res, end - start + 1);
            
            ++end;
        }

        return res;
    }
};
