class Solution {
    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int first = 0; first < nums.length; first++) {
            int targetKey = target - nums[first];
            if (map.containsKey(targetKey)) {
                int second = map.get(targetKey);
                return new int[]{second, first};
            }
            map.put(nums[first], first);
        }

        return null;
    }
}
