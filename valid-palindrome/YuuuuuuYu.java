/**
 * Runtime: 2ms
 * Time Complexity: O(n)
 *
 * Memory: 44.29MB
 * Space Complexity: O(1)
 *
 * Approach: 투 포인터
 * 1) 문자열의 양 끝에서부터 시작하는 두 포인터를 설정
 * 2) 포인터가 가리키는 문자가 영숫자가 아닌 경우, 해당 포인터를 이동
 */
class Solution {
    public boolean isPalindrome(String s) {
        int start = 0;
        int end = s.length()-1;

        while (start < end) {
            char currLeft = s.charAt(start);
            char currRight = s.charAt(end);

            if (!Character.isLetterOrDigit(currLeft)) {
                start++;
            } else if (!Character.isLetterOrDigit(currRight)) {
                end--;
            } else {
                if (Character.toLowerCase(currLeft) != Character.toLowerCase(currRight)) {
                    return false;
                }

                start++;
                end--;
            }
        }

        return true;
    }
}
