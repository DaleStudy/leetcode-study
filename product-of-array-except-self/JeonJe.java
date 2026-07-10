import java.util.*;

// TC: O(n)
// SC: O(1)
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;

        int[] answer = new int[n];
        answer[0] = 1;
        for (int i = 1; i < n; i++) {
            answer[i] = answer[i - 1] * nums[i - 1];
        }

        int right = 1;
        for (int i = n - 2; i >= 0; i--) {
            right = right * nums[i + 1];
            answer[i] = answer[i] * right;
        }
        return answer;
    }
}
