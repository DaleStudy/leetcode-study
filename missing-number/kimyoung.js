var missingNumber = function (nums) { // brute force approach
    let missingNumber;
    for (let i = 0; i < nums.length; i++) {
        if (nums.indexOf(i) === -1) missingNumber = i;
    }
    return missingNumber === undefined ? nums.length : missingNumber;
};

// time - O(n^2) finding the index of i while iterating through nums
// splace - O(1) no extra space needed other than missingNumber which just stores the result

var missingNumber = function (nums) { // set approach 
    let set = new Set(nums);
    for (let i = 0; i < nums.length + 1; i++) {
        if (!set.has(i)) return i;
    }
};

// time - O(n) looping through nums to find the missing number
// splace - O(n) creating a set of nums

var missingNumber = function (nums) { // mathematical approach
    const len = nums.length
    const expectedSum = len * (len + 1) / 2;
    const actualSum = nums.reduce((acc, el) => acc += el, 0);
    return expectedSum - actualSum;
};

// time - O(n) reduce method on actualSum
// space - O(1) extra space irrelevant to input
