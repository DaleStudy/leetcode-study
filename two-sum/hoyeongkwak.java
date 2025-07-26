/*
time complexity : O(n)
space complexity : O(n)
*/
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> sumMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int secondNum = target - nums[i];
            if (sumMap.containsKey(secondNum)) {
                return new int[] { sumMap.get(secondNum), i };
            }
            sumMap.put(nums[i], i);
        }
        return new int[] {};
    }
}
