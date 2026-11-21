// Time: O(n)
// Space: O(1)
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;

        array<int, 26> freq1{}, freq2{};
        for (char c: s) freq1[c - 'a']++;
        for (char c: t) freq2[c - 'a']++;

        return freq1 == freq2;
    }
};
