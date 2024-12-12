/*
    Problem: https://leetcode.com/problems/valid-palindrome/
    Description: return true if it is a palindrome, alphanumeric characters(letters and numbers) reads the same forward and backward
    Concept: Two Pointers, String
    Time Complexity: O(n), Runtime: 10ms
    Space Complexity: O(n), Memory: 58.6MB
*/
class Solution {
    public boolean isPalindrome(String s) {
        String regex ="[^A-Za-z0-9]";
        String palindrome = s.replaceAll(regex,"").toLowerCase(); //replaceAll(), toLowerCase(): O(n)

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
