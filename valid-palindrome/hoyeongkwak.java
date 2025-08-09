/*
Time Complexity : O(n)
Space Complexity : O(n)
*/
class Solution {
    public boolean isPalindrome(String s) {
        if (s.length() == 1) return true;
        String sLower = s.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");
        StringBuffer strBuilder = new StringBuffer(sLower);
        String revStr = strBuilder.reverse().toString();
        return sLower.equals(revStr);
    }
}
