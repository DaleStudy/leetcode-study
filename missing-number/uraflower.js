/**
 * @param {number[]} nums
 * @return {number}
 */
const missingNumber = function(nums) {
    const n = nums.length;
    let sum = (n * (n + 1)) / 2;

    for (let num of nums) {
        sum -= num;
    }
    
    return sum;
};

// 시간복잡도: O(n)
// 공간복잡도: O(1)
