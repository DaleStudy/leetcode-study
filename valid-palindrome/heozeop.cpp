// Time Complexity: O(n)
// Spatial Complexity: O(n)

class Solution {
public:
    bool isPalindrome(string s) {
        string temp = "";
        for(char c : s) {
            if(isalnum(c)) {
                temp += tolower(c);
            }
        }

        int length = temp.length();
        for(int i = 0; i < length / 2; ++i) {
            if(temp[i] != temp[length - 1 - i]) {
                return false;
            }
        }

        return true;
    }
};
