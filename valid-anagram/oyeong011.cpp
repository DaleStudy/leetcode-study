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

