/*
    Problem: https://leetcode.com/problems/two-sum/
    Description: return indices of the two numbers such that they add up to target. not use the same element twice.
    Topics: Array, Hash Table
    Time Complexity: O(N), Runtime 2ms
    Space Complexity: O(N), Memory 45.1MB
*/
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numIndex = new HashMap<>();
        for(int secondIndex=0; secondIndex<nums.length; secondIndex++){
            if(numIndex.containsKey(target-nums[secondIndex])){
                int firstIndex = numIndex.get(target-nums[secondIndex]);
                return new int[]{firstIndex, secondIndex};
            } else {
                numIndex.put(nums[secondIndex], secondIndex);
            }
        }
        return new int[]{};
    }
}
