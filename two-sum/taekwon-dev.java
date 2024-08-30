/**
 * 시간/공간 복잡도: O(n)
 */
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int idx = 0; idx < nums.length; idx++) {
            int complement = target - nums[idx];
            if (map.containsKey(complement)) {
                return new int[]{map.get(complement), idx};
            }
            map.put(nums[idx], idx);
        }

        return new int[]{-1, -1};
    }
}
