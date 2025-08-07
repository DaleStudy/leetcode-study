import java.util.*;
// 2번째 풀이
class Solution {
    public int rob(int[] nums) {
        int[] dp = new int[nums.length+1];
        dp[1] = nums[0];

        for(int i = 1; i < nums.length; i++){
            dp[i+1] = Math.max(dp[i-1] + nums[i], dp[i]);
        }
        return dp[nums.length];
    }
}



// 1번째 풀이
class Solution {
    public int rob(int[] nums) {
        int[] house = new int[nums.length];
        Arrays.fill(house, -1);
        return maxRobbery(0, nums, house);
    }

    private int maxRobbery(int index, int[] nums, int[] house) {
        if (index >= nums.length) return 0;
        if (house[index] != -1) return house[index];

        int rob = nums[index] + maxRobbery(index + 2, nums, house);
        int skip = maxRobbery(index + 1, nums, house);

        house[index] = Math.max(rob, skip);
        return house[index];
    }
}

