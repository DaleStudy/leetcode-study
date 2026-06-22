class Solution {
    // TC : O(n)
    // SC : O(1)
    public boolean isPalindrome(String s) {
        // Condition 1 : after converting all uppercase letters into lowercase letters
        // and removing all non-alphanumeric characters
        String onlyAlphaNumeric = s.toLowerCase().replaceAll("[^a-z0-9]", "");
        int length = onlyAlphaNumeric.length();
        for (int i = 0; i < length / 2; i++) {
            int right = length - 1 - i;
            int left = i;
            // Condition 2 : it reads the same forward and backward
            if (onlyAlphaNumeric.charAt(left) != onlyAlphaNumeric.charAt(right))
                return false;
        }
        return true;
    }
}
