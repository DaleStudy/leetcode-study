class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();    // convert into lowercase letters
        s = s.replaceAll("[^a-zA-Z0-9]", "");  // remove non-alphanumeric characters
        int start = 0;
        int end = s.length()-1;

        while (start < end) {
            char startChar = s.charAt(start);
            char endChar = s.charAt(end);

            if (startChar != endChar) {
                return false;
            }

            ++start;
            --end;
        }

        return true;
    }
}