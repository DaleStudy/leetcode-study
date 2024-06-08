- 문제: https://leetcode.com/problems/container-with-most-water/
- time complexity : O(n)
- space complexity : O(1)
- 블로그 주소 : https://algorithm.jonghoonpark.com/2024/06/02/leetcode-11

```java
class Solution {
    public int maxArea(int[] height) {
        int start = 0;
        int end = height.length - 1;

        int max = getArea(height, start, end);

        while(start < end) {
            if(height[start] >= height[end]) {
                end--;
                max = Math.max(max, getArea(height, start, end));
            } else {
                start++;
                max = Math.max(max, getArea(height, start, end));
            }
        }

        return max;
    }

    public int getArea(int[] height, int start, int end) {
        if (start == end) {
            return 0;
        }
        return getMinHeight(height[end], height[start]) * (end - start);
    }

    public int getMinHeight(int height1, int height2) {
        return Math.min(height1, height2);
    }
}
```
