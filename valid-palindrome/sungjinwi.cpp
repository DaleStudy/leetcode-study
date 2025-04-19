/*
    풀이 :
        alnum인 문자들만 추출해서 소문자로 만들어 alnu_s를 만듬
        양 끝이 같은 문자일 동안 left++, right-- 실시
        같지 않으면 false, 양 끝이 수렴되서 서로 만난다면 true
    
    문자 길이 N

    TC : O(N)

    SC : O(N)
*/

#include <string>
using namespace std;

class Solution {
    public:
        bool isPalindrome(string s) {
            string alnu_s = "";
    
            for (char c : s)
            {
                if (isalnum(c))
                    alnu_s += tolower(c);
            }
            int left = 0;
            int right = alnu_s.size() - 1;
            while (left < right)
            {
                if (alnu_s[left] != alnu_s[right])
                    return false;
                left++;
                right--;
            }
            return true;
        }
    };
