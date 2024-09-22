// 시간복잡도: O(n)
// 공간복잡도: O(1)

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let maxArea = 0;

    let leftIdx = 0;
    let rightIdx = height.length - 1;

    while (leftIdx <= rightIdx) {
        const minHeight = Math.min(height[leftIdx], height[rightIdx]);
        const distance = rightIdx - leftIdx

        maxArea = Math.max(maxArea, distance * minHeight);

        if (height[leftIdx] < height[rightIdx]) leftIdx++
        else rightIdx--
    }

    return maxArea
};

console.log(maxArea([1,8,6,2,5,4,8,3,7])) //49
console.log(maxArea([1,1])) //1
