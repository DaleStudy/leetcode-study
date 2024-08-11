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
                int start = i, end = j, flag = 0;

                while (start <= end) {
                    if (s[start] != s[end]) {
                        flag = 1;
                        break;
                    }
                    start++;
                    end--;
                }

                if (!flag) res++;
            }
        }

        return res;
    }
};