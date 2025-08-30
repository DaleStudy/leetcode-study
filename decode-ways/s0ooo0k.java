class Solution {
    public int numDecodings(String s) {
        if(s.charAt(0)=='0') return 0;
        
        int n = s.length();
        int[] dp = new int[n+1];

        dp[0]=1;
        dp[1]=1;

        for(int i=2; i<=n; i++) {
            if(s.charAt(i-1)!='0') dp[i]+=dp[i-1];

            int group = Integer.parseInt(s.substring(i-2, i));
            if(group>=10 && group<=26) {
                dp[i]+=dp[i-2];
            }
        }
        return dp[n];
    }
}

