/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let max = 0;

    let startIdx = 0;
    let endIdx = height.length - 1;

    while (startIdx < endIdx) {
        const start = height[startIdx];
        const end = height[endIdx];

        const gap = endIdx - startIdx;
        const min = Math.min(start, end);

        const area = gap * min;

        max = Math.max(max, area);

        if (start < end) startIdx++;
        else endIdx--;
    }

    return max;
};

// 시간복잡도 O(n)
// n은 주어진 배열(height)의 길이


