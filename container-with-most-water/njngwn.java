// Time Complexity: O(n), n: height.length
// Space Complexity: O(1)
class Solution {
    public int maxArea(int[] height) {
        int maxWaterAmount = 0;
        int leftLineIdx = 0;
        int rightLineIdx = height.length-1;

        while (leftLineIdx < rightLineIdx) {
            int leftHeight = height[leftLineIdx];
            int rightHeight = height[rightLineIdx];
            int tempAmount = 0;

            if (leftHeight < rightHeight) {
                tempAmount = leftHeight * (rightLineIdx - leftLineIdx);
                leftLineIdx++;
            } else {
                tempAmount = rightHeight * (rightLineIdx - leftLineIdx);
                rightLineIdx--;
            }

            // update maximum amount
            maxWaterAmount = tempAmount > maxWaterAmount ? tempAmount : maxWaterAmount;
        }

        return maxWaterAmount;
    }
}