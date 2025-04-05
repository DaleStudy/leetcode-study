/**
 * <a href="https://leetcode.com/problems/two-sum/">week01-2.two-sum</a>
 * <li> Description: return indices of the two numbers such that they add up to target. not use the same element twice. </li>
 * <li> Topics: Array, Hash Table             </li>
 * <li> Time Complexity: O(N), Runtime 2ms    </li>
 * <li> Space Complexity: O(N), Memory 45.4MB </li>
 */

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = target - nums[i];

            if (seen.containsKey(num))
                return new int[]{seen.get(num), i};

            seen.put(nums[i], i);
        }

        throw new IllegalArgumentException();
    }
}
