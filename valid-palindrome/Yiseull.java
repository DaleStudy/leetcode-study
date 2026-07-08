class Solution {
    public boolean isPalindrome(String s) {
        /**
        첫 번째 풀이: 시간복잡도 O(n), 공간복잡도 O(n)
        String letters = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        String reverse = new StringBuilder(letters).reverse().toString();
        return letters.equals(reverse);
         */

        // 두 번째 풀이: 시간복잡도 O(n), 공간복잡도 O(1)
         int left = 0, right = s.length() - 1;
         while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }

            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }

            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }

            left++;
            right--;
         }

         return true;
    }
}
