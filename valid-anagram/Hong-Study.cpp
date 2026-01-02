'''
Time Complexity: O(n log n)
- 분류 정렬에서 O(n log n) 발생

Run time 
- 7ms

Memory
- 9.56 MB

최적화쪽으로 수정 추가 필요
'''
class Solution {
public:
    bool isAnagram(string s, string t) {
        // 선 길이 체크
        if (s.length() != t.length()) {
            return false;
        }

        // 두 배열 정렬(n log n)
        std::sort(s.begin(), s.end());
        std::sort(t.begin(), t.end());

        // 비교하여 다르면 false
        for (int i = 0; i < s.length(); i++) {
            if (s[i] != t[i]) {
                return false;
            }
        }

        return true;
    }
};
