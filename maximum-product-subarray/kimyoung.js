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

// time - O(n^3) double for loop * reduce()
// space - O(1) 

var maxProduct = function (nums) { // DP approach
    let result = nums[0];
    let [min, max] = [1, 1];

    for (const num of nums) {
        [min, max] = [Math.min(num * min, num * max, num), Math.max(num * min, num * max, num)];
        result = Math.max(max, result);
    }

    return result;
};

// time - O(n) looping through nums once
// space - O(1) extra memory irrelevant to input
