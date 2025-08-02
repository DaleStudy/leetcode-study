// 모든 철자가 있는지 확인
class Solution {
public:
    bool isAnagram(string s, string t) {
        // 1. 문자열 정렬
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        // 2. 비교
        if (s.compare(t) == 0)
            return 1;
        
        return 0;
    }
};

