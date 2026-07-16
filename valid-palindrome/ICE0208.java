class Solution {

    public boolean isPalindrome(String s) {
        /*
         * 문제에서는 대소문자를 구분하지 않고,
         * 알파벳과 숫자만 남긴 뒤 팰린드롬인지 확인한다.
         *
         * Character.isLetterOrDigit(ch)는
         * 현재 문자가 알파벳 또는 숫자인지 확인하는 함수다.
         * 공백, 쉼표, 콜론 같은 문자는 비교 대상이 아니므로 건너뛴다.
         *
         * 입력은 printable ASCII 문자로 제한되어 있으므로
         * charAt()으로 한 문자씩 확인해도 된다.
         *
         * 시간 복잡도: O(n)
         * 공간 복잡도: O(1)
         */
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }

            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }

            char leftChar = Character.toLowerCase(s.charAt(left));
            char rightChar = Character.toLowerCase(s.charAt(right));

            if (leftChar != rightChar) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
}
