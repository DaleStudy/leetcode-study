class Solution {
    public boolean isPalindrome(String s) {
        /**
        1. 문제: 팰린드롬인지 판단하는 문제.
        2. 조건: 알파벳 소문자로 변환, 문자 또는 숫자가 아닌건 모두 제거 (공백, 쉼표 등))
        - left, right index 이중 포인터로 풀이
        time complexity : O(n)
        space complexity : O(1)
         */
         boolean answer = true;
         //문자열 추가하면 space complexity : O(n)
         //s = s.toLowerCase();
         //s = s.replaceAll("[^0-9a-z]", "");
         int left = 0 ;
         int right = s.length() - 1;

        while(left < right) {
            char l = s.charAt(left);
            char r = s.charAt(right);

            //왼쪽이 알파벳 or 숫자가 아니면 skip
            if (!Character.isLetterOrDigit(l)) {
                left += 1;
                continue;
            }
            //오른쪽이 알파벳 or 숫자가 아니면 skip
            if (!Character.isLetterOrDigit(r)) {
                right -= 1;
                continue;
            }
            if (Character.toLowerCase(l) != Character.toLowerCase(r) ) {
                return false;
            }
            left += 1;
            right -= 1;
        }
        
        return answer;
    }
}
