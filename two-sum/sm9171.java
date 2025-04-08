class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int gap = target - nums[i];
            if(hashMap.containsKey(gap)){
                int j = hashMap.get(gap);
                return new int[]{i,j};
            }
            hashMap.put(nums[i], i);
        }
        return null;
    }
}
