/**
 * 구하려는 것은 최대 영역값이기 때문에 x,y축을 계산한 현재 영역과 기존 영역을 비교해 max값을 반환하면 됩니다.
 * 포인터를 어떻게 좁힐까 생각할 수 있는데 쉽게 말해서 start와 end 중 더 작은 쪽을 앞 또는 뒤로 이동하면 됩니다.
 * 영역은 두 막대가 모두 충족가능한 길이가 되어야 하므로 Math.min()으로 설정합니다.
 */
class Solution {
    public int maxArea(int[] height) {
        int start = 0;
        int end = height.length - 1;
        int area = 0;

        while (start < end) {
            int y = Math.min(height[start], height[end]); // y축은 더 작은 값으로 설정
            int x = Math.abs(start - end); // end - start도 가능
            int calculatedArea = x * y;
            area = Math.max(area, calculatedArea);

            // [중요] 포인터 이동 로직
            if (height[start] <= height[end])
                start++;
            else
                end--;
        }
        return area;
    }
}
