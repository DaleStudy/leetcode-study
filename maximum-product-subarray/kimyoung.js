var maxProduct = function (nums) { // brute force approach - doesn't pass leetcode (Time Limit Exceeded)
    let maxProduct = -Infinity;
    for (let i = 0; i < nums.length; i++) { // get subarrays
        for (let j = i; j < nums.length; j++) {
            let prod = nums.slice(i, j + 1).reduce((acc, el) => acc *= el, 1);
            maxProduct = Math.max(prod, maxProduct);
        }
    }
    return maxProduct;
};

// time - O(n^2) double for loop
// space - O(n^2) total count of subarrays = n*(n+1)/2


// TODO - different approach
