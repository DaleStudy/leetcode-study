class Solution {
    public int[] twoSum(int[] nums, int target) {
        // time complexity: O(n);
        // space complexity: O(n);
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) map.put(nums[i], i);

        for (int i = 0; i < nums.length; i++) {
            int candidateKey = target - nums[i];
            if (map.containsKey(candidateKey) && i != map.get(candidateKey))
                return new int[]{i, map.get(candidateKey)};
        }
        return new int[]{-1, -1};
    }
}
