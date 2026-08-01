import java.util.*;

// TC: O(n)
// SC: O(1)
class Solution {
    public int maxArea(int[] height) {
        int n = height.length;
        int left = 0;
        int right = n - 1;

        int answer = calWaterArea(height, left, right);

        while (left < right) {
            if (height[left] <= height[right]) {
                left++;
            } else {
                right--;
            }
            answer = Math.max(answer, calWaterArea(height, left, right));
        }
        return answer;
    }

    private static int calWaterArea(int[] height, int left, int right) {
        return getLowerHeight(height, left, right) * (right - left);
    }

    private static int getLowerHeight(int[] height, int left, int right) {
        return Math.min(height[left], height[right]);
    }
}
