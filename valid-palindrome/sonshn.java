/**
 * Palindrome 문자열인지 확인하는 문제
 * 
 * Java에서 제공하는 Character.isLetterOrDigit() 메서드를 사용하여 알파벳과 숫자인지 확인하고,
 * Character.toLowerCase() 메서드를 사용하여 대소문자를 구분하지 않고 비교
 * 
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(1)
 */
class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {

            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }

            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }

            if (Character.toLowerCase(s.charAt(left))
                    != Character.toLowerCase(s.charAt(right))) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
}
