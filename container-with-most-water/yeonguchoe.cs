using System;

public class Solution {
    public int MaxArea(int[] height) {
        int currentMax = int.MinValue;
        int leftPtr = 0;
        int rightPtr = height.Length - 1;

        while (leftPtr < rightPtr) {
            int currentAmount = (rightPtr - leftPtr) * Math.Min(height[leftPtr], height[rightPtr]);
            currentMax = Math.Max(currentMax, currentAmount);

            if (height[leftPtr] < height[rightPtr]) {
                leftPtr++;
            } else {
                rightPtr--;
            }
        }

        return currentMax;
    }
}
