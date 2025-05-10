class Solution {

    /**
     * time-complexity : O(n)
     * space-complexity : O(1)
     */

    public int maxArea(int[] height) {

        int left = 0;
        int right = height.length - 1;

        int w = 0, h = 0, currSize = 0, maxSize = 0;

        while (left < right) {

            w = right - left;
            h = Math.min(height[left], height[right]);

            currSize = w * h;
            maxSize = Math.max(currSize, maxSize);

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }

        }
        return maxSize;
    }
}
