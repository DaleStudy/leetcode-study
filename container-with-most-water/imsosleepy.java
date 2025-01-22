// 투포인터를 활용한 시간복잡도 O(N)으로 풀면된다.
// 중요한건 언제 이동하냐?를 정의하는건데, 전체 물양이 줄어들면 상대적으로 작은 쪽을 이동시키면된다.
class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length-1;
        int maxWater = 0;
        while(left < right) {
            int max = Math.min(height[left], height[right]) * (right - left);
            maxWater = Math.max(max,maxWater);
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxWater;
    }
}
