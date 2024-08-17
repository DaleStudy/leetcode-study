// 시간복잡도: O(n)
// 공간복잡도: O(n)

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const map = new Map()

    for (let i = 0; i < nums.length; i++) {
        map.set(nums[i], (map.get(nums[i]) || 0) + 1);
    }

    const buckets = Array.from({length: nums.length + 1}, () => [])

    for (const [num, frequency] of map.entries()) {
        buckets[frequency].push(num);
    }

    const result = [];
    for (let i = buckets.length - 1; i >= 0 && result.length < k; i--) {
        result.push(...buckets[i]);
    }

    return result.slice(0, k);

};

console.log(topKFrequent([1,1,1,2,2,3],2))
