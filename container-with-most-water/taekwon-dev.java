/**
 *  시간 복잡도: O(n)
 *  공간 복잡도: O(1)
 *
 *  최대로 많은 물을 저장하기 위해 가장 우선적으로 고려해야 하는 것은 짧은 막대의 길이
 *  따라서, 짧은 높이를 가지는 쪽의 포인터를 이동하면서 최대 저장 가능한 값을 비교
 *
 */
class Solution {
    public int maxArea(int[] height) {
        int answer = 0;
        int left = 0;
        int right = height.length - 1;

        while (left < right) {
            int water = Math.min(height[left], height[right]) * (right - left);
            answer = Math.max(answer, water);

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return answer;
    }
}
