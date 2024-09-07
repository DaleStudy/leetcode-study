/**
 * 풀이
 * - 주어진 string `s`의 양 끝에서부터 차례대로 비교해가며 palindrome 여부를 판단합니다
 * 
 * Big-O
 * - N: 주어진 string `s`의 길이
 * 
 * - Time Complexity: O(N)
 *   - `s`가 palindrome인 경우, `s` 전체를 탐색하므로 O(N)의 시간복잡도를 가집니다
 * 
 * - Space Complexity: O(1)
 *   - 입력값과 무관하게 일정한 저장공간을 사용합니다
 */

class Solution {
public:
    bool isPalindrome(string s) {
        string::iterator lo = s.begin();
        string::iterator hi = s.end();

        while (lo <= hi) {
            if (isalnum(*lo) && isalnum(*hi)) {
                if (tolower(*lo) != tolower(*hi)) return false;
                else {
                    ++lo;
                    --hi;
                    continue;
                }
            }
            if (!isalnum(*lo)) ++lo;
            if (!isalnum(*hi)) --hi;
        }

        return true;
    }
};
