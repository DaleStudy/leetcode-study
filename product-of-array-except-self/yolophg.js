// Time Complexity: O(n)
// Space Complexity: O(n)

var productExceptSelf = function(nums) {
    const n = nums.length;
    const leftProducts = new Array(n).fill(1);
    const rightProducts = new Array(n).fill(1);
    const result = new Array(n);

    // leftProduct will be the product of all elements to the left of index i.
    for (let i = 1; i < n; i++) {
        leftProducts[i] = leftProducts[i - 1] * nums[i - 1];
    }

    // rightProduct will be the product of all elements to the right of index i.
    for (let i = n - 2; i >= 0; i--) {
        rightProducts[i] = rightProducts[i + 1] * nums[i + 1];
    }

    // result will be the product of leftProduct and rightProduct.
    for (let i = 0; i < n; i++) {
        result[i] = leftProducts[i] * rightProducts[i];
    }

    return result;
};
