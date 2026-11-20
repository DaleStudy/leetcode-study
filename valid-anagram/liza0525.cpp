// TC: O(n)
//   - s(또는 t)의 문자열 길이 만큼 for 루프를 돈다.
// SC: O(n)
//   - mapper의 key는 서로 다른 문자의 개수만큼만 생긴다.
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;  // 길이가 다르면 early return

        // 각 문자를 key로, 문자 개수를 value로 하는 mapper 정의
        unordered_map<char, int> mapper;

        for (int i=0; i < s.size(); i++) {
            // 각 문자들에 대해서
            // s의 i번째 문자에 대해 mapper에 value를 1 증가
            // t의 i번째 문자에 대해 mapper에 value를 1 감소
            mapper[s[i]]++;
            mapper[t[i]]--;
        }

        for (auto& [k, v]: mapper) {
            // 위의 for문 결과로 value가 0이 아닌 문자가 있다면 즉시 false로 리턴
            if (v != 0) return false;
        }

        return true;
    }
};
