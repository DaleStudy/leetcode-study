class Solution {
    int[] numOfWays = new int[101];

    public int numDecodings(String s) {
        return dfs(s, 0);
    }

    public int dfs(String s, int cur) {
        if (cur == s.length()) {
            return 1;
        }

        int cnt = 0;

        if (cur + 1 <= s.length() && isDecodable(s.substring(cur, cur + 1))){
            if (numOfWays[cur + 1] == 0){
                numOfWays[cur + 1] = dfs(s, cur + 1);
            }
            cnt += numOfWays[cur + 1];
        }

        if (cur + 2 <= s.length()&& isDecodable(s.substring(cur, cur + 2))) {
            if (numOfWays[cur + 2] == 0){
                numOfWays[cur + 2] = dfs(s, cur + 2);
            }
            cnt += numOfWays[cur + 2];
        }

        return cnt;
    }

    public boolean isDecodable(String s) {
        if (s.startsWith("0")){
            return false;
        }
        int digit = Integer.valueOf(s);
        return (digit >= 1 && digit <= 26);
    }
}


