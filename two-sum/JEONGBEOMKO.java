import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numberMap = new HashMap<>();
        for (int i=0; i<nums.length; i++) {
            numberMap.put(nums[i], i);
        }

        for(int i=0; i<nums.length; i++) {
            int operand = target - nums[i];
            if (numberMap.containsKey(operand) && numberMap.get(operand) != i) { // 자기 자신은 제외
                return new int[] { numberMap.get(target - nums[i]), i };
            }
        }

        return new int[] {};
    }
}
