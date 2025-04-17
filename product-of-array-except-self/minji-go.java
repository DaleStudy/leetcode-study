/**
 <a href="https://leetcode.com/problems/product-of-array-except-self/">week02-3.product-of-array-except-self</a>
 <li> Description: return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].</li>
 <li> Concept: Array, Prefix Sum                                        </li>
 <li> Time Complexity: O(N), Runtime 2ms                                </li>
 <li> Space Complexity: O(1), Memory 55.62MB - except the output array  </li>
 */
class Solution {
    public int[] productExceptSelf(int[] nums) {

        int[] answer = new int[nums.length];
        Arrays.fill(answer, 1);

        int left = 1;
        for(int i=1; i<nums.length; i++) {
            answer[i] *= left *= nums[i-1];
        }

        int right = 1;
        for(int i=nums.length-2; i>=0; i--) {
            answer[i] *= right *= nums[i+1];
        }

        return answer;
    }
}
