/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let result = 0
    let l = 0;
    let r = height.length - 1;

    while(l < r) {
        const area = (r - l) * Math.min(height[l], height[r]);
        result = Math.max(result, area);

        if(height[l] < height[r]) {
            l += 1;
        } else {
            r -= 1;
        }
    }
    return result
};
