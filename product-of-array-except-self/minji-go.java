/*
    Problem: https://leetcode.com/problems/product-of-array-except-self/
    Description: return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
    Concept: Array, Prefix Sum
    Time Complexity: O(N), Runtime 5ms
    Space Complexity: O(N), Memory 54.6MB - O(1) except the output array
*/
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        Arrays.fill(answer, 1);

        int prefixProduct = 1;
        int suffixProduct = 1;
        for(int i=1; i<nums.length; i++){
            prefixProduct = prefixProduct * nums[i-1];
            suffixProduct = suffixProduct * nums[nums.length-i];
            answer[i] *= prefixProduct;
            answer[nums.length-i-1] *= suffixProduct;
        }

        return answer;
    }
}
