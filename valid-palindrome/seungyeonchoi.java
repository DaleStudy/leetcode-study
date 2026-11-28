/**
Approach
- remove non-alphanumeric character
- compare characters from both ends, moving toward the middle.

Complexity
- time: O(N), use 2 for-loop
- space: O(N), create char array with size the same as given String s, create string value which the size is within given String s
 */
class Solution {
    public boolean isPalindrome(String s) {
        char[] arr = s.toCharArray();
        StringBuilder sb = new StringBuilder();
        for(char ch: arr) {
            // At first, I didn't know this func
            if (Character.isAlphabetic(ch) || Character.isDigit(ch)) {
                sb.append(ch);
            }
        }

        arr = sb.toString().toLowerCase().toCharArray();
        for (int i =0 ; i<sb.length()/2; i++) {
            if (arr[i]!=arr[sb.length()-1-i]) {
                return false;
            }
        }
        return true;
    }
}
