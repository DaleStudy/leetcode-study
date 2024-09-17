// TC:
// SC:
class Solution {
    public int maxArea(int[] height) {
        int max = 0;

        int start = 0;
        int end = height.length-1;

        while (start < end) {
            int heightLeft = height[start];
            int heightRight = height[end];

            int hei = Math.min(heightLeft, heightRight);
            int wid = end - start;

            max = Math.max(max, hei*wid);

            if (heightRight > heightLeft) start += 1;
            else end -= 1;
        }
        return max;
    }
}
