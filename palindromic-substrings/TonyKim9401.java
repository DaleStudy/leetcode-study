class Solution {
    public int countSubstrings(String s) {
        /**
         * time complexity: O(n);
         * space complexity: O(1);
         */

        int output = 0;
        // ex) abc
        // 1. abc
        // 2. bc
        // 3. c
        for (int i = 0; i < s.length(); i++) {
            output += palindromicCheck(s.substring(i, s.length()));
        }
        return output;
    }

    public int palindromicCheck(String str) {
        int result = 0;
        /**
         * ex) abc
         * 1. a
         * 2. ab
         * 3. abc
         */
        for (int i = 0; i < str.length(); i++) {
            String candidate = str.substring(0, i+1);
            if (palindromic(candidate)) {
                result += 1;
            }
        }
        return result;
    }

    public boolean palindromic(String candidate) {
        int start = 0;
        int end = candidate.length() - 1;

        /** ex)abc
         * 1. a -> true
         * 2. ab -> false
         * 3. abc -> false
         */
        while (start < end) {
            if (candidate.charAt(start) != candidate.charAt(end)) return false;
            start += 1;
            end -= 1;
        }
        return true;
    }
}