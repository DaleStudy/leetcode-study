import java.util.*;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] right = new int[n + 1];
        int[] left = new int[n + 1];

        right[0] = 1;
        for (int i = 1; i <= n; i++) {
            right[i] = right[i - 1] * nums[i - 1];
        }

        left[n] = 1;
        for (int i = n - 1; i >= 0; i--) {
            left[i] = left[i + 1] * nums[i];
        }

        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            answer[i] = right[i] * left[i + 1];
        }

        return answer;
    }
}
