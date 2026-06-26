import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numIndexMap = new HashMap<>();

        for (int i=0; i<nums.length; i++) {
            int need = target - nums[i];
            if (numIndexMap.containsKey(need)) {
                return new int[]{numIndexMap.get(need), i};
            }
            numIndexMap.put(nums[i], i);
        }

        return new int[]{};
    }
}
