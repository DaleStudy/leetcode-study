/*
    Problem: https://leetcode.com/problems/palindromic-substrings/
    Description: return the number of palindromic substrings in it.
    Concept: Two Pointers, String, Dynamic Programming
    Time Complexity: O(N²), Runtime 6ms
    Space Complexity: O(1), Memory 41.62MB
*/
class Solution {
    public int countSubstrings(String s) {
        int totalCount = 0;
        for(int i=0; i<s.length(); i++){
            totalCount+= countPalindromes(s, i, i);
            totalCount+= countPalindromes(s, i, i+1);
        }
        return totalCount;
    }

    public int countPalindromes(String s, int left, int right){
        int count = 0;
        while(left>=0 && right<s.length() && s.charAt(left)==s.charAt(right)) {
            count++;
            right++;
            left--;
        }
        return count;
    }
}
