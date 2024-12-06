class Solution {
public:
    bool isPalindrome(string s) {
        string clean = "";
        for(char c : s) {
            if(isalnum(c)) {
                clean += tolower(c);
            }
        }
        
        string reversed = clean;
        reverse(reversed.begin(), reversed.end());

        return clean == reversed;
    }
};