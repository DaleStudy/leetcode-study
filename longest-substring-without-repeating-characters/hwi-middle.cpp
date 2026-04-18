class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        unordered_map<char, int> m; // 현재 윈도우 내에 있는 문자 - 인덱스
        int maxLen = 0;
        int l = 0;
        for (int r = 0; r < n; ++r)
        {
            if (m.contains(s[r])) // 중복된 문자를 찾은 경우
            {
                l = max(m[s[r]] + 1, l); // 해당 문자가 l보다 뒤에 있다면 l을 거기로 옮김
            }

            m[s[r]] = r; // s[r]의 위치 업데이트

            maxLen = max(maxLen, r - l + 1);
        }

        return maxLen;
    }
};
