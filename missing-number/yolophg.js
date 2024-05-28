// Time Complexity: O(n)
// Space Complexity: O(1)

var missingNumber = function(nums) {
    const n = nums.length;
    // sum of numbers from 0 to n.
    const expectedSum = (n * (n + 1)) / 2; 
    // sum of numbers in the array.
    const actualSum = nums.reduce((acc, curr) => acc + curr, 0); 

    // the difference is the missing number.
    return expectedSum - actualSum; 
};
