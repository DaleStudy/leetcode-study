class Solution {
    int n;

    public int lengthOfLIS(int[] nums) {
        int answer = 1;
        n = nums.length;

        // TreeMap<Integer, Integer> sequence = new TreeMap<>();
        int[] dp = new int[n];
        dp[n-1] = 1;

        // sequence.put(nums[n-1], n-1);

        for (int i = n-2; i >= 0; i--) {
            Integer key = findKey(nums[i], i, dp, nums);
            if (key == null) {
                dp[i] = 1;
            }
            else {
                dp[i] = 1 + dp[key];
            }
            answer = Math.max(dp[i], answer);
            // sequence.put(nums[i], i);
        }

        for (int i = 0; i < n; i++) {
            System.out.print(dp[i] + " ");
        }
        return answer;
    }

    public Integer findKey(int key, int idx, int[] dp, int[] nums) {
        Integer retKey = null;
        int maxLength = 0;

        for (int i = idx + 1; i < n; i++) {
            if ((nums[idx] < nums[i]) && (1 + dp[i]) > maxLength) {
                maxLength = 1 + dp[i];
                retKey = i;
            }
        }
        return retKey;
    }

}


