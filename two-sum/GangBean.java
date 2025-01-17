class Solution {
    public int[] twoSum(int[] nums, int target) {
        /**
            1. understanding
            - find the indices where the numbers of that index pair sum upto the target number.
            - exactly one solution
            - use each element only once
            - return in any order
            2. strategy
            - brute force:
                - validate for all pair sum
            - hashtable:
                - assing hashtable variable to save the nums and index
                - while iterate over the nums,
                - calculate the diff, and check if the diff in the hashtable.
                - or save new entry.
            3. complexity
            - time: O(N)
            - space: O(N)
        */

        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (map.containsKey(diff)) {
                return new int[] {map.get(diff), i};
            }
            map.put(nums[i], i);
        }

        return new int[] {};
    }
}

