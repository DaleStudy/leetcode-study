import java.util.*;

// TC: O(log n)
// SC: O(1)
class Solution {
    public int findMin(int[] nums) {

        int lowIndex = 0;
        int highIndex = nums.length - 1;

        while(lowIndex < highIndex) {
            int midIndex = (lowIndex + highIndex) / 2;

            //오른 부분이 정렬 되지 않음 = 왼쪽 부분은 정렬됨
            if(nums[midIndex] > nums[highIndex]) {
                lowIndex = midIndex + 1;
            } else {
                //오른쪽 부분이 정렬 됨 = 왼쪽 부분을 봐야함
                highIndex = midIndex;
            }
        }
        return nums[lowIndex];
    }
}
