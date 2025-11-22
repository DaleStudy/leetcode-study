import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// link: https://leetcode.com/problems/3sum/
// difficulty: Medium
class Solution {
    // Problem:
    // * return: all triplets of elements in nums such that the sum == 0 (indices must differ)
    // Solution:
    // * Time Complexity: O(N^2)
    // * Space Complexity: O(1)
    public List<List<Integer>> threeSum(int[] nums) {
        // sort for simplicity
        // Time Complexity: O(N log N)
        Arrays.sort(nums);

        List<List<Integer>> answers = new ArrayList<>();

        // if there are only positive or only negative numbers, there exist no solution
        if(nums[0] > 0 || nums[nums.length-1] < 0) return answers;



        // Time Complexity: O(N^2)
        // * for loop * inner while loop = O(N) * O(N) = O(N^2)

        // nums[i]: first of the triplet
        // * skip positive because the other two will also be positive
        for(int i = 0; i < nums.length && nums[i] <= 0; i++) {
            // skip if same first of the triplet met
            if(i != 0 && nums[i] == nums[i-1]) continue;

            int numI = nums[i];

            int left = i + 1;
            int right = nums.length - 1;

            // Time Complexity: O(N)
            while(left < right) {
                int numLeft = nums[left];
                int numRight = nums[right];

                int sum = numI + numLeft + numRight;

                if(sum == 0) {
                    answers.add(Arrays.asList(numI, numLeft, numRight));

                    // skip same lefts and rights two prevent duplicate
                    // * must update both left and right
                    //    * e.g. if only left is moved, newNumLeft = 0 - (numI + numRight) and that can only be numLeft that's already visited
                    // * Time Complexity: O(1) because there is no actual operation other than skipping
                    while(left < nums.length && nums[left] == numLeft) left++;

                    while(right > left && nums[right] == numRight) right--;
                } else if(sum > 0) {
                    right--;
                } else {
                    left++;
                }
            }
        }

        return answers;
    }
}
