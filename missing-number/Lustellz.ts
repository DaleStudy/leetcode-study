// Runtime: 18ms
// Memory: 58.64MB

function missingNumber(nums: number[]): number {
    const sortedNums: number[] = nums.sort((a, b) => a - b);
    for(let i = 0; i <= nums.length; i++){
        if(sortedNums[i] !== i) return i
    }
};

// Runtime: 1ms
// Memory: 58.34MB
// reduce sum of array to find missing number

function missingNumber(nums: number[]): number {
    const n: number = nums.length;
    const numSum: number = nums.reduce((acc, cur) => (acc += cur), 0);
    const expectedSum: number = (n * (n + 1)) / 2;

    return expectedSum - numSum;
}
