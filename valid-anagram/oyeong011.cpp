class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> ss, tt;
        if(s.length() != t.length())return false;
        for(auto i : s) ss[i]++;
        for(auto i : t) tt[i]++;
        return ss == tt;
    }
};

// 문자열 비교 unordered_map은 해쉬 형태이므로 O(1)
// 각 문자 루프 O(n)
// 마지막 문자 비교 해시멥 알파벳은 26개 이므로 O(n)
// 따라서 O(n)