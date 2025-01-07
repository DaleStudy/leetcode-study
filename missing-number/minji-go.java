/*
    Problem: https://leetcode.com/problems/missing-number/
    Description: return the only number in the range that is missing from the array.
    Concept: Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting
    Time Complexity: O(N), Runtime 0ms
    Space Complexity: O(1), Memory 45.71MB
*/
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int missing = n;

        for(int i=0; i<n; i++){
            missing ^= i;
            missing ^= nums[i];
        }
        return missing;
    }
}
