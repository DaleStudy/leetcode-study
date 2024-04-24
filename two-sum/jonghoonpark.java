/*
 * https://leetcode.com/problems/two-sum/
 * time complexity : O(n)
 * space complexity : O(n)
 * https://jonghoonpark.com/2024/01/03/leetcode-1
 */

/*
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int _target = target - num;

            if (numMap.containsKey(_target)) {
                return new int[]{numMap.get(_target), i};
            }
            numMap.put(num, i);
        }

        return null;
    }
}
*/