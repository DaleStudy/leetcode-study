import java.util.HashMap;
import java.util.Map;
/*
시간복잡도: O(n)
공간복잡도: O(n)
 */

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numberMap = new HashMap<>();
        for (int i=0; i<nums.length; i++) {
            numberMap.put(nums[i], i);
        }

        for(int i=0; i<nums.length; i++) {
            int operand = target - nums[i];
            if (numberMap.containsKey(operand) && numberMap.get(operand) != i) {
                return new int[] { numberMap.get(target - nums[i]), i };
            }
        }

        return new int[] {};
    }
}
