class Solution {
public:
    bool isPalindrome(string s) {
        int len = s.size();
        int l = 0;
        int r = len - 1;

        while (l <= r)
        {
            while (l <= r &&!isalnum(s[l]))
            {
                l++;
            }

            while (l <= r && !isalnum(s[r]))
            {
                r--;
            }

            if (l > r)
            {
                break;
            }

            if (tolower(s[l]) != tolower(s[r]))
            {
                return false;
            }

            l++;
            r--;
        }

        return true;
    }
};
