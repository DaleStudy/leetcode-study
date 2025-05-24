class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0;
        int s = 0, e = height.length - 1;

        while (s < e) {
            int h = Math.min(height[s], height[e]);
            int area = (e - s) * h;
            maxArea = Math.max(maxArea, area);

            if (height[s] < height[e]) {
                s++;
            } else {
                e--;
            }
        }

        return maxArea;
    }
}

