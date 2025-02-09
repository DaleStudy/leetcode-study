class Solution {
    /** 시간 : O(n), 공간 : O(1)*/
    fun maxArea(height: IntArray): Int {
        var maxDiff = 0
        var left = 0
        var right = height.lastIndex
        // left, right값을 순차적으로 조회해서 물높이를 구하고,
        // left < right값 보다 작으면 left증가시킨다. 반대는 right 감소
        while (left < right) {
            maxDiff = max(maxDiff, (right - left) * min(height[left], height[right]))
            // 너비 : right - left
            // 현재 높이 :  min(height[left], height[right])
            // 너비 * 현재 높이가 maxDiff 비교하여 더 큰값이 maxDiff가 된다.
            if (height[left] < height[right]) {
                left++
            } else {
                right--
            }
        }
        return maxDiff
    }
}
