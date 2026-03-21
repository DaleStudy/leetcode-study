/*
    A phrase is a palindrome if,
    after converting all uppercase letters into lowercase letters and
    removing all non-alphanumeric characters, it reads the same forward and backward.
    Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.

    Example 1:

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

    Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
*/

#include <cctype>
#include <string>
#include <vector>
using namespace std;

#pragma region ExtraSpaceIdea
// 새로운 배열을 만들어서 문자열을 정리한 후에 팰린드롬 판별
// 시간 복잡도 : O(n)
// 공간 복잡도 : O(n)
// n은 문자열의 길이일 것이다.
namespace extra_space_idea {

class Solution {
public:
    bool isPalindrome(string s) {
        vector<char> str;
        str.reserve(s.size());

        size_t len = s.length();
        for (size_t i = 0; i < len; i++) {
            if (isalnum(s[i])) {
                str.push_back(tolower(s[i]));
            }
        }

        size_t vec_len = str.size();
        for (size_t i = 0; i < (vec_len + 1) / 2; i++) {
            if (str[i] != str[vec_len - 1 - i]) return false;
        }

        return true;
    }
};

}  // namespace extra_space_idea
#pragma endregion

#pragma region FinalSolution
// 투 포인터를 이용해 추가 배열 없이 구현
// 시간 복잡도 : O(n)
// 공간 복잡도 : O(1)
class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.length() - 1;

        while(left < right) {
            if (!isalnum(s[left]))
                left++;
            else if (!isalnum(s[right]))
                right--;
            else {
                if (tolower(s[left]) != tolower(s[right]))
                    return false;
                left++;
                right--;
            }
        }

        return true;
    }
};
#pragma endregion
