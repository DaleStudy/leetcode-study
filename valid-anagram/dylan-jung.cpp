class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;
        unordered_map<char, int> m1;
        unordered_map<char, int> m2;
        for(char c: s) m1[c]++;
        for(char c: t) m2[c]++;
        for(auto const& item: m1) {
            if(m2[item.first] != item.second) return false;
        }
        return true;
    }
};
