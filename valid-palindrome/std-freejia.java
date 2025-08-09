class Solution {
    public boolean isPalindrome(String s) {
        String alphabetOnly = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        return new StringBuilder(alphabetOnly).reverse().toString().equals(alphabetOnly);
    }
}
