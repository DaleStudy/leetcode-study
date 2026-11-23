// Time: O(n), Space: O(1)
class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size() - 1;

        while(l < r) {
            while(l < r && !isalnum(s.at(l))){
                l++;
            }

            while(l < r && !isalnum(s.at(r))){
                r--;
            }

            if(tolower(s.at(l)) != tolower(s.at(r))){
                return false;
            }

            l++;
            r--;
        }

        return true;
    }
};
