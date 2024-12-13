/*
Runtime: 1 ms(Beats: 100.00 %)
Time Complexity: O(n)

Memory: 43.00 MB(Beats: 64.54 %)
Space Complexity: O(1)
... 문제에서 주어진 String s는 space complexity 계산에서 제외하고, 제가 추가한 변수에 대해서만 계산하면 될까요?
*/

class Solution {
    public boolean isPalindrome(String s) {
        for (int i = 0, j = s.length() - 1; i < j; i++, j--) {
            char a = s.charAt(i);
            while (a < '0' || (a > '9' && a < 'A') || (a > 'Z' && a < 'a') || a > 'z') {
                a = s.charAt(++i);
                if (i >= j) {
                    return true;
                }
            }
            if (a <= 'Z') {
                a += ('a' - 'A');
            }

            char b = s.charAt(j);
            while (b < '0' || (b > '9' && b < 'A') || (b > 'Z' && b < 'a') || b > 'z') {
                b = s.charAt(--j);
                if (i >= j) {
                    return true;
                }
            }
            if (b <= 'Z') {
                b += ('a' - 'A');
            }

            if (a != b) {
                return false;
            }
        }
        return true;
    }
}
