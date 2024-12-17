/*
Runtime: 2 ms(Beats: 99.10 %)
Time Complexity: O(n)

Memory: 42.75 MB(Beats: 85.31 %)
Space Complexity: O(1)
... 문제에서 주어진 String s는 space complexity 계산에서 제외하고, 제가 추가한 변수에 대해서만 계산하면 될까요?

ps. 처음 풀이에서는 alphanumeric 여부와 대소문자 관련 로직을 일일이 구현했다가, isLetterOrDigit(), toLowerCase()로 변경했습니다.
*/

class Solution {
    public boolean isPalindrome(String s) {
        for (int i = 0, j = s.length() - 1; i < j; i++, j--) {
            char a = s.charAt(i);
            while (!Character.isLetterOrDigit(a)) {
                a = s.charAt(++i);
                if (i >= j) {
                    return true;
                }
            }
            a = Character.toLowerCase(a);

            char b = s.charAt(j);
            while (!Character.isLetterOrDigit(b)) {
                b = s.charAt(--j);
                if (i >= j) {
                    return true;
                }
            }
            b = Character.toLowerCase(b);

            if (a != b) {
                return false;
            }
        }
        return true;
    }
}
