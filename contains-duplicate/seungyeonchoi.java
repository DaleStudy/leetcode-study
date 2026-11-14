class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> duplicates = new HashSet<>();
        for (int i=0; i<nums.length;i++) {
            // duplicates.add(nums[i]);
            // if (duplicates.size() != i+1) {
            //     return true;
            // }
            if (!duplicates.add(nums[i])) {
                return true;
            }
        }
        return false;
    }

    /*
    complexity
    - time: O(n) using a for loop
    - space: O(n) declaring a set
    */

}
