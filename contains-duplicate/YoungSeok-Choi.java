class Solution {
    // 시간복잡도 O(n)
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Boolean> dupMap = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            if(dupMap.containsKey(nums[i])) {
                return true;
            }

            dupMap.put(nums[i], true);
        }

        return false;
    }
}