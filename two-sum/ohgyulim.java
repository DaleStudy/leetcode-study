import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numToIndex = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int remains = target - nums[i];
            if (numToIndex.containsKey(remains)) {
                return new int[]{i, numToIndex.get(remains)};
            }
            numToIndex.put(nums[i], i);
        }
        return null;
    }
}

