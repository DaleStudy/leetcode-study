/*
https://leetcode.com/problems/two-sum/
 */
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }

        for(int i = 0; i < nums.length; i++) {
            if(map.containsKey(target - nums[i]) && map.get(target - nums[i]) != i) {
                int j = map.get(target - nums[i]);
                return new int[]{i, j};
            }
        }

        return null;
    }
}
