class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        /**
        1.문제: s 가 wordDict 로 쪼개질 수 있는지 true/false return
        2.조건
        - s 에는 wordDict 가 여러번 나올 수 있음.
        - s.length() 최소 = 1, 최대 300
        - wordDict.size() 최소 1, 최대 1000
        - 한 단어 길이 최소=1, 최대 = 20
        - 모두 소문자. 모든 wordDict 값은 unique
        3.풀이
        - i번째까지 문자열을 만들 수 있는지 check
         */

         int n = s.length();
         boolean[] dp = new boolean[n+1];

         dp[0] = true;  //빈 문자열인 경우

         for(int i = 1; i < n+1; i++) {
            for(int j = 0; j < i; j++) {
                String subStr = s.substring(j, i);
                //앞단계 모두 만들 수 있고 && wordDict에 존재하는지 체크
                if(dp[j] && wordDict.contains(subStr)) {
                    dp[i] = true;
                    break; 
                }
            }
         }
        return dp[n];
    }
}
