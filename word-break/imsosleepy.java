// dp 배열 (dp[i] = s[0...i]가 단어들로 나눠질 수 있는지 여부)
// 입력 데이터의 크기가 크지 않아서 O(N^2)도 가능한 문제.
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        boolean[] dp = new boolean[s.length() + 1];  
        dp[0] = true; 
        
        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordSet.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        
        return dp[s.length()]; 
    }
}
