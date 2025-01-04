// 완전탐색을 통해 모든 경우의 수를 구하기 위해 노력하였지만 시간초과가 발생하였습니다.
// dfs를 통해 풀이하려고 했지만 O(2^N)의 시간복잡도로 인해 시간초과가 발생하였습니다.
// 이후 dp로 풀이를 시작하였고 어렵지 않게 풀이하였습니다.
// dp[i] = dp[i-1] + dp[i-2]로 풀이하였습니다.
// 이때 i번째 문자열을 1자리로 취급할지 2자리로 취급할지에 따라 경우의 수가 달라집니다.
// 1자리로 취급할 경우 1~9까지 가능하고
// 2자리로 취급할 경우 10~26까지 가능합니다.

// 시간복잡도 : O(N)
// 공간복잡도 : O(N)
class SolutionGotprgmer {
    public int numDecodings(String s) {
        // 예외 처리: 문자열이 "0"으로 시작하거나 빈 문자열이면
        if (s == null || s.length() == 0 || s.charAt(0) == '0') {
            return 0;
        }
        int[] dp = new int[s.length()+1];
        dp[0] = 1;
        for(int i=0;i<s.length();i++){
            int ith = s.charAt(i)-'0';
            if(ith != 0){
                dp[i+1] = dp[i];
            }
            if(i>0){
                String twoDigitStr = s.substring(i-1,i+1);
                int twoDigitNum = Integer.valueOf(twoDigitStr);
                if(twoDigitNum>=10 && twoDigitNum <27){
                    dp[i+1] += dp[i-1];
                }
            }

        }
        return dp[s.length()];
    }


}
