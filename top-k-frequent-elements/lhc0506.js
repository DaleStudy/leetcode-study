/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const numsMap = {};

    nums.forEach(num => {
        numsMap[num] ? numsMap[num] += 1 : numsMap[num] = 1;
    });

    return Object.entries(numsMap).sort((a, b) => b[1] - a[1]).slice(0, k).map(([key]) => Number(key));
};
