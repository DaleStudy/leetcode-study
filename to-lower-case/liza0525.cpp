// TC: O(n) - s의 길이만큼 시간이 걸림
// SC: O(1) - 추가 자료구조 없이 기존 문자열 변경
class Solution {
public:
    string toLowerCase(string s) {
        for (std::size_t i = 0; i < s.size(); i++) {
            if (std::isupper(s[i])){
                s[i] = std::tolower(s[i]);
            }
        }
        return s;
    }
};

