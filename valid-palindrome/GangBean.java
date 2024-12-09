class Solution {
    public boolean isPalindrome(String s) {
        /**
         * Step 1: Convert the input string to lowercase. -> O(n)
         * Step 2: Remove all non-alphanumeric characters using regex. -> O(n)
         * Step 3: Use two pointers to compare characters from both ends of the string. -> O(n)
         * Total time complexity: O(n), where n is the length of the string.
         */
        s = s.toLowerCase();
        s = s.replaceAll("[^a-z0-9]", "");
        int left = 0;
        int right = s.length() - 1;
        if (right <= 0) return true;
        while (left < right) {
            if (s.charAt(left++) != s.charAt(right--)) return false;
        }
        return true;
    }
}

