class Solution {
public:
    void compare(string s, int left, int right, int& max_start, int& max_end){
        while(left >= 0 && right < s.length() && s[left] == s[right]){
            left--;
            right++;
        }

        if(max_end - max_start < right - left - 1){
            max_start = left + 1;
            max_end = right - 1;
        }
    }

    string longestPalindrome(string s) {
        int max_start = 0;
        int max_end = 0;

        for(int i = 0; i < s.length(); i++){
            compare(s, i, i, max_start, max_end);
            compare(s, i, i + 1, max_start, max_end);
        }

        return s.substr(max_start, max_end - max_start + 1);
    }
};
