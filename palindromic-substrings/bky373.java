// time: O(N^3) (the worst case)
// space: O(1)
class Solution {

    public int countSubstrings(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j < s.length(); j++) {
                count += isPalindrome(s, i, j);
            }
        }
        return count;
    }

    int isPalindrome(String s, int start, int end) {
        while (start < end) {
            if (s.charAt(start) != s.charAt(end)) {
                return 0;
            }
            start++;
            end--;
        }
        return 1;
    }
}
