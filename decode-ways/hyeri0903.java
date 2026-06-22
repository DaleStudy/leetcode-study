class Solution {
    public int numDecodings(String s) {
        /**
        1.문제: decode 할 수 있는 모든 경우의 수 return
        2.조건:
        - 여러 개의 경우의 수 있을 수 있다. 
        - decode 불가능한 경우가 있을 수 있다.
        - 모두 불가능한 경우 return 0
        3.풀이
        - dp (해석할 수 있는 방법 수를 누적해서 더함)
        e.g 226 
        0자리 : dp[0] = 0
        1자리(2) : 2 -> dp]1] = 1
        2자리(22): 2(B), 22(v) -> dp[2] = 2
        3자리(226): (2, 2, 6), (22, 6), (2, 26) -> dp[3] = 3

        time complexity: O(N)
        space complexity: O(N)

         */
         if (s.charAt(0) == '0') {
            return 0;
         }
         int n = s.length();
         int[] dp = new int[n+1];
         dp[0] = 1; //아무것도 없는 상태
         dp[1] = 1;
        
        for(int i = 2; i<=n; i++) {
            //1자리수
            if (s.charAt(i-1) != '0') {
                dp[i] += dp[i-1];
            }
            //2자리수
            if(i > 1) {
                int number = Integer.parseInt(s.substring(i-2, i));
                //2자리 수는 10 ~ 26사이만 가능
                if (number >= 10 && number <= 26) {
                    dp[i] += dp[i-2];
                }
            }
        }
        return dp[n];
    }
}
