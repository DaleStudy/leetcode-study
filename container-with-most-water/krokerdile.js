/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let left = 0;
    let right = height.length - 1;
    let max = 0;

    while(right > left){
        if(height[left] >= height[right]){
            max = Math.max(max, height[right] * (right - left));
            right = right -1;
        }
        else{
            max = Math.max(max, height[left] * (right - left));
            left = left +1;
        }
    }
    return max;
};
