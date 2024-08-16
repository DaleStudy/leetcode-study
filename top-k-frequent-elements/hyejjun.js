/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
    const count = {};

    nums.forEach((num) => {
        count[num] = (count[num] || 0) + 1;
    });

    const filtered = Object.keys(count).sort((a, b) => count[b] - count[a]);

    return filtered.slice(0, k).map(Number);

};

console.log(topKFrequent([1, 1, 1, 2, 2, 3], 2)); // [1, 2]
console.log(topKFrequent([1], 1)); // [1]

/*
Time Complexity : O(NLogN)
Space Complexity: O(N)
*/