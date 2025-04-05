import java.util.*;
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