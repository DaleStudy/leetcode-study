/**
 * For the length N of given string s,
 * 
 * Time complexity: O(N^3)
 * 
 * Space complexity: O(1)
 */

class Solution {
public:
    int countSubstrings(string s) {
        int res = 0;

        for (int i = 0; i < s.size(); i++) {
            for (int j = i; j < s.size(); j++) {
                int start = i, end = j;
                bool is_palindrome = true;

                while (start <= end) {
                    if (s[start] != s[end]) {
                        is_palindrome = false;
                        break;
                    }
                    start++;
                    end--;
                }

                if (is_palindrome) res++;
            }
        }

        return res;
    }
};