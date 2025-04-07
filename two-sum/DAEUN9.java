import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> existedMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int remain = target - nums[i];
            if (existedMap.containsKey(remain)) {
                return new int[]{existedMap.get(remain), i};
            }
            existedMap.put(nums[i], i);
        }
        return new int[]{0, 0};
    }
}
