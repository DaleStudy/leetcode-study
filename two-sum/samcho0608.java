import java.util.HashMap;
import java.util.Map;

class Solution {
    // return: indices of two numbers that add up to `target`
    // * exactly one solution
    // * must use index only once

    // Time Complexity: O(n)
    // Space Complexity: O(n)
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> indexByNum = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            int numI = nums[i];
            indexByNum.put(numI, i);
        }

        for(int i = 0; i < nums.length; i++) {
            int numI = nums[i];
            Integer compl = indexByNum.getOrDefault(target-numI, null);
            if(compl != null && i != compl) return new int[] {i, compl};
        }

        return null;
    }
}
