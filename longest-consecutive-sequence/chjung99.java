class Solution {
    int[] dp;
    int[] next;
    int n;
    Map<Integer, Integer> location;

    public int longestConsecutive(int[] nums) {
        n = nums.length;
        dp = new int[n];
        next = new int[n];
        location = new HashMap<>();

        for (int i = 0; i < n; i++){
            location.put(nums[i], i);
            dp[i] = -1;
        }

        for (int i = 0; i < n; i++){
            int nextValue = nums[i] + 1;
            if (location.containsKey(nextValue)) {
                next[i] = location.get(nextValue);
                continue;
            }
            next[i] = -1;
        }

        for (int i = 0; i < n; i++) {
            if (next[i] == -1) {
                dp[i] = 1;
                continue;
            }
            if (dp[next[i]] == -1) {
                dp[i] = 1 + find(next[i], nums);
                continue;
            }
            if (dp[next[i]] != -1){
                dp[i] = 1 + dp[next[i]];
            }
        }
        int answer = 0;
        for (int i = 0; i < n; i++){
            // System.out.print(dp[i] + " ");
            answer = Math.max(answer, dp[i]);
        }
        return answer;
    }

    public int find(int idx, int[] nums) {
        if (next[idx] == -1) {
            dp[idx] = 1;
        }
        else if (dp[next[idx]] == -1) {
            dp[idx] = 1 + find(next[idx], nums);
        }
        else if (dp[next[idx]] != -1) {
            dp[idx] = 1 + dp[next[idx]];
        }
        return dp[idx];
    }


}


