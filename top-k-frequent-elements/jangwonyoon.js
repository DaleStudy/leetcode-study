/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

/*
 * 시간 복잡도: O(n log n)
 * 공간 복잡도: O(n)
 *
 * 1. map 구조를 사용해서 몇번 나왔는지 카운트한다.
 * 2. map 구조에서 가장 큰 수를 구한다.
*/
var topKFrequent = function(nums, k) {
    const map = new Map();

    for (let i = 0; i < nums.length; i++) {
        if (!map.has(nums[i])) {
            map.set(nums[i], 1);
        } else {
            map.set(nums[i], map.get(nums[i]) + 1);
        }
    }

    const result = [...map.entries()].sort((a, b) => b[1] - a[1]);

    return result.slice(0, k).map((val) => val[0]);
};
