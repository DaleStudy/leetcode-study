class Solution {
    public int maxArea(int[] height) {
        /**
        1. understanding
        - with two pair of line, each can contain "min(line1,line2) * (distance)" mount of water
        - find maximum amount of water can contain
        2. strategy
        - brute force
            - for each pair of lines, calculate amount and update maximum amount.
            - it can takes O(N), where N is the count of lines.
            - N is 10^5 at most, so it can takes 10^10, which can takes about 10 seconds
        - you need to swap out unnecessary calculation
        - so, let's find a unnecessary calculation in this problem.
        3. complexity
        - time: O(N)
        - space: O(1)
        */
        int l = 0;
        int r = height.length - 1;
        int maxAmount = amountOf(height, l, r); // Math.min(height[l], height[r], r-l);
        while (l < r) { // O(N)
            maxAmount = Math.max(maxAmount, amountOf(height, l, r));
            if (height[l] < height[r]) {
                l++;
            } else if (height[l] > height[r]) {
                r--;
            } else {
                int nextLeftAmount = amountOf(height, l+1, r);
                int nextRightAmount = amountOf(height, l, r-1);
                if (nextLeftAmount < nextRightAmount) {
                    r--;
                } else {
                    l++;
                }
            }
        }

        return maxAmount;
    }

    private int amountOf(int[] height, int left, int right) {
        return (Math.min(height[left], height[right]) * (right - left));
    }
}

