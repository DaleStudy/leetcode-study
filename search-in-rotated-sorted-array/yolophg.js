// Time Complexity: O(n)
// Space Complexity: O(1)

var search = function(nums, target) {
    // iterate through each element.
    for (let i = 0; i < nums.length; i++) {
        // check if the current element is equal to the target.
        if (nums[i] === target) {
            // if found, return the index.
            return i;
        }
    }

    // if the loop completes without finding the target, return -1.
    return -1;
};
