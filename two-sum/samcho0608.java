import java.util.HashMap;
import java.util.Map;

// link: https://leetcode.com/problems/two-sum/description/
// difficulty: Easy
class Solution {
    // Problem
    // * exactly one solution
    // * must use index only once
    // * return: indices of two numbers that add up to `target`
    // Solution:
    // * Time Complexity: O(N)
    // * Space Complexity: O(N)
    public int[] twoSum(int[] nums, int target) {
        // Space Complexity: O(N)
        Map<Integer, Integer> indexByNum = new HashMap<>();

        // Time Complexity: O(N)
        for(int i = 0; i < nums.length; i++) {
            int numI = nums[i];
            indexByNum.put(numI, i);
        }

        // Time Complexity: O(N)
        for(int i = 0; i < nums.length; i++) {
            int numI = nums[i];
            Integer compl = indexByNum.getOrDefault(target-numI, null);

            if(compl != null && i != compl)
                return new int[] {i, compl};
        }

        return null;
    }
}
