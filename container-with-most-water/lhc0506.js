/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let result = 0;
    let left = 0;
    let right = height.length - 1;

    while(left < right) {
        const leftHeight = height[left];
        const rightHeight = height[right];
        const width = right - left;

        const minHeight = leftHeight < rightHeight ? leftHeight : rightHeight;
        const area = minHeight * width;

        if (area > result) {
            result = area;
        }

        if (leftHeight <= rightHeight) {
            left++;
        } else {
            right--;
        }
    }
    return result;
};

// 시간 복잡도: O(n)
// 공간 복잡도: O(1)
