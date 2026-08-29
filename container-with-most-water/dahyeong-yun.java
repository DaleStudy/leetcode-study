/**
  * TC : O(n)
  *   - 기둥 높이 배열의 길이 n에 대해 최악의 경우 전체를 순회 하므로 O(n)
  * SC : O(1)
  *   - 별도로 유의미한 공간 생성이 없음
  */
class Solution {
    /**
     * 넗이의 조합을 다 해보고 max 값을 찾으면 됨
     * 그 중에 안해도 되는 조합이 있음. 더 낮은 높이로 인해서 넓이가 결정되므로 더 높은 탑은 그냥 유지하고 다른 조합만 확인해보면 됨.
     */
    public int maxArea(int[] height) {
        int left = 0, right = height.length-1, max = 0;
        while(left < right) {
            int w = right - left;
            int h = height[left] < height[right] ? height[left] : height[right];

            int current = w * h;
            max = Math.max(max, current);

            if(height[left] > height[right]) right --;
            else left ++;
        }
        return max;
    }
}
