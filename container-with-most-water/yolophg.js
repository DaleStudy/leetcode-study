// Time Complexity: O(n)
// Space Complexity: O(1)

var maxArea = function(height) {
    let left = 0;
    let right = height.length - 1;

    // to store the maximum area.
    let maxArea = 0;

    // iterate until the two pointers meet.
    while (left < right) {
        // calculate the width between the two pointers.
        let width = right - left;

        // calculate the area with the current area.
        let currentArea = Math.min(height[left], height[right]) * width;

        // update the maximum area if the current area is larger.
        maxArea = Math.max(maxArea, currentArea);

        // move the pointer to the shorter line towards the center.
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    // return the maximum area found.
    return maxArea;
};
