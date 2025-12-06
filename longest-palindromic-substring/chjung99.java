// brute force
// time: O(N^3)
// space: O(N)

class Solution {
    public String longestPalindrome(String s) {
        String answer = "";
        int maxLen = 0;
        int sLen = s.length();

        for (int i = 0; i < sLen; i++){
            for (int j = i ; j < sLen; j++){
                String substring = s.substring(i, j+1);
                if (isPalindrom(substring) && maxLen < (j-i+1)){
                    maxLen = (j-i+1);
                    answer = substring;
                }
            }
        }

        return answer;
    }

    public boolean isPalindrom(String s){
        int start = 0;
        int end = s.length()-1;


        while(start < end) {
            if (s.charAt(start) == s.charAt(end)){
                start++;
                end--;
            } else {
                return false;
            }
        }

        return true;
    }

}


