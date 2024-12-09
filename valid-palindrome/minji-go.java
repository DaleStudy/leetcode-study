class Solution {
    public boolean isPalindrome(String s) {
        String regex ="[^A-Za-z0-9]";
        String palindrome = s.replaceAll(regex,"").toLowerCase();

        boolean answer = true;
        for(int i=0; i<palindrome.length()/2; i++){
            if(palindrome.charAt(i) != palindrome.charAt(palindrome.length()-1-i)) {
                answer = false;
                break;
            }
        }
        return answer;
    }
}