class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase().trim();
        s = s.replaceAll("[^a-z0-9]", "");

        StringBuffer sb = new StringBuffer(s);
        String reverse = sb.reverse().toString();

        return(s.equals(reverse));

    }
}