/*
 * https://leetcode.com/problems/valid-palindrome/
 * time complexity : O(n)
 * space complexity : O(n)
 * https://jonghoonpark.com/2024/04/24/leetcode-125
 */

/*

void main() {
    Solution solution = new Solution();
    System.out.println(solution.isPalindrome("A man, a plan, a canal: Panama")); // true
    System.out.println(solution.isPalindrome("race a car")); // false
    System.out.println(solution.isPalindrome(" ")); // true
}

class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder filtered = new StringBuilder();
        for(char c : s.toCharArray()) {
            // '0' == 48, '9' == 57, 'A' == 65, 'z' == 122
            if ((c >= '0' && c <= '9') || (c >= 'a' && c <= 'z')) {
                filtered.append(c);
            } else if ((c >= 'A' && c <= 'Z')) {
                filtered.append((char) (c + 32));
            }
        }

        for(int i = 0; i < filtered.length() / 2; i++) {
            if (filtered.charAt(i) != filtered.charAt(filtered.length() - i - 1)) {
                return false;
            }
        }

        return true;
    }
}

*/