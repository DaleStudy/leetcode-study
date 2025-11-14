import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // 시간 복잡도를 생각해서 HashMap을 사용

        Map<Integer, Integer> idx = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int c = target - nums[i];
            if (idx.containsKey(c)) {
                return new int[]{idx.get(c), i};
            }
            idx.put(nums[i], i);
        }
        return new int[]{};
    }
}