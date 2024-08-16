class Solution {
    public boolean containsDuplicate(int[] nums) {
        // HashSet  O(n)
        /*
        Set<Integer> set = new HashSet();
        for (int num : nums) set.add(num);
        return set.size() != nums.length;
        */

        // dupl value O(n log n)
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) return true;
        }
        return false;
    }
}