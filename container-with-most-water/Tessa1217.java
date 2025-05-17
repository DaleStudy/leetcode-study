/**
 * 정수 배열 height가 주어질 때 물을 최대한 담을 수 있는 두 개의 라인을 찾으세요.
 힌트1. 투 포인터를 활용해서 찾으세요.
 */
class Solution {

    // 시간 복잡도: O(n)
    public int maxArea(int[] height) {

        int max = 0;
        int start = 0;
        int end = height.length - 1;

        while (start < end) {

            int area = Math.min(height[start], height[end]) * (end - start);
            max = Math.max(area, max);

            if (height[start] < height[end]) {
                start++;
            } else {
                end--;
            }
        }

        return max;
    }
}

