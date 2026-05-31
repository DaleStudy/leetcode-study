class Solution {
public:
    bool isPalindrome(string s) {
        string p;
        for(char const& c: s) {
            if('A' <= c && c <= 'Z') {
                p.push_back(c - 'A' + 'a');
            }
            else if('a' <= c && c <= 'z') {
                p.push_back(c);
            }
            else if ('0' <= c && c <= '9') {
                p.push_back(c);
            }
        }
        int start = 0, end = p.size()-1;
        while(start <= end) {
            if(p[start++] != p[end--]) return false;
        }
        return true;
    }
};
