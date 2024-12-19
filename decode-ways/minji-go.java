/*
    Problem: https://leetcode.com/problems/decode-ways/
    Description: Given a string s containing only digits, return the number of ways to decode it
    Concept: String, Dynamic Programming
    Time Complexity: O(N), Runtime 1ms
    Space Complexity: O(N), Memory 42.12MB
*/
class Solution {
    public int numDecodings(String s) {
        int[] dp = new int[s.length()];
        if(decode(s.substring(0, 1))) dp[0]=1;
        if(s.length()>1 && decode(s.substring(1, 2))) dp[1]+=dp[0];
        if(s.length()>1 && decode(s.substring(0, 2))) dp[1]+=dp[0];

        for(int i=2; i<s.length(); i++){
            if(decode(s.substring(i,i+1))) dp[i]+=dp[i-1];
            if(decode(s.substring(i-1,i+1))) dp[i]+=dp[i-2];
        }
        return dp[s.length()-1];
    }

    public boolean decode(String s){
        int num = Integer.parseInt(s);
        int numLength = (int) Math.log10(num) + 1;
        if(num<0 || num>26 || numLength != s.length()) return false;
        return true;
    }
}
