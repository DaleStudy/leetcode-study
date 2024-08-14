/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
    let result = [];
    let fObj = {};

    for (let i = 0; i < nums.length; i++) {
        const n = nums[i];
        fObj[n] ? fObj[n]++ : fObj[n] = 1;
    }

    Object
        .entries(fObj)
        .sort((a, b) => b[1] - a[1])
        .slice(0, k)
        .filter(v => result.push(v[0]));

    return result;
};
