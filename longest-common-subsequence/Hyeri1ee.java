import java.util.*;
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
    
        
        //int longerlen= (text1.length() >= text2.length()) ? text1.length() : text2.length();
        //int lesslen= (text1.length() <= text2.length()) ? text1.length() : text2.length();
        int[][] dp = new int[text1.length()+1][text2.length()+1];

        //String longertext= (text1.length() >= text2.length()) ? text1 : text2;
        //String lesstext= (text1.length() <= text2.length()) ? text1 : text2;



        for (int i = 1; i <=text1.length(); i++) {
            for (int j = 1; j <=text2.length(); j++) {
                //문자가 같으면
                if (text1.charAt(i-1) == text2.charAt(j-1)){
                    dp[i][j] = dp[i-1][j-1]+1; 
                    //System.out.println("dp["+i+"]["+j+"]: "+ dp[i][j]);
                }else{
                    //문자가 다르면
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                    //System.out.println("dp["+i+"]["+j+"]: "+ dp[i][j]);
                }
            }
        }


        return dp[text1.length()][text2.length()];
    }//end of method
}

