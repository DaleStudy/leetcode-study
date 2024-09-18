/**
 * https://leetcode.com/problems/container-with-most-water/
 * time complexity : O(n)
 * space complexity : O(1)
 */
export function maxArea(height: number[]): number {
    let s = 0, e = height.length - 1, max = 0;

    while (s < e) {
        max = Math.max((e - s) * Math.min(height[s], height[e]), max);
        if (height[s] < height[e]) s++;
        else e--;
    }
    return max;
};
