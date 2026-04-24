class Solution {
    public int countSubstrings(String s) {
         /**
        1.문제: s 에서 palindromoic substring 개수 return
        2.constraints:
        - 연속적인 문자
        - s.length min = 1, max = 1000
        3.풀이
        -  bruteforce: time:O(n^3), space:O(n)
        - expand around : time(On^2), space:O(1)
         */

         int n = s.length();
         if(n == 1) return 1;
        int count = 0;

        for(int i = 0; i < n; i++) {
            //odd
            count += checkPalindrome(s, i, i);

            //even
            count += checkPalindrome(s, i, i+1);
        }
        return count;

    }

    private int checkPalindrome(String s, int left, int right) {
        int count = 0;
        while(left >= 0 && right < s.length() && s.charAt(right) == s.charAt(left)) {
            count += 1;
            left -= 1;
            right += 1;
        }
        return count;
    }

}
