// Time Complexity: O(log n)
// Space Complexity: O(1)

var findMin = function(nums) {
    // initialize left pointer.
    let left = 0;
    // initialize right pointer.
    let right = nums.length - 1;

    while (left < right) {
        // calculate the middle index.
        let mid = left + ((right - left) / 2 | 0);

        // if the value at the middle index is bigger, move the left pointer to the right.
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else { // else, move the right pointer to the middle index.
            right = mid;
        }
    }

    // return the element which is the minimum pointed to by the left pointer.
    return nums[left];
};
