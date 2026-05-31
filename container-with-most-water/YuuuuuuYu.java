/**
 * Runtime: 3ms
 * Time Complexity: O(n)
 *
 * Memory: 77.24MB
 * Space Complexity: O(1)
 *
 * Approach: 좌우 높이 중 더 작은 높이 기준으로 계산하기 때문에 그 높이를 최대한 높일 수 있는 방향으로 포인터 이동
 * - while문 내에서 현재 포인터의 높이보다 같거나 작은 높이를 건너뛰도록 최적화
 */
class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length-1;
        int max = 0;

        while (left < right) {
            int hLeft = height[left];
            int hRight = height[right];
            int currentArea = (right-left) * Math.min(hLeft, hRight);
            if (currentArea > max) {
                max = currentArea;
            }

            if (hLeft < hRight) {
                left++;
                while (left < right && height[left] <= hLeft) {
                    left++;
                }
            } else {
                right--;
                while (left < right && height[right] <= hRight) {
                    right--;
                }
            }
        }

        return max;
    }
}
