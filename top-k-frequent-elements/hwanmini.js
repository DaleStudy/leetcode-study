// 시간복잡도: O(n log n)
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

    const frequencyArr  = [...map]
    const sortedArr = frequencyArr.toSorted((a,b) => b[1] - a[1])

    return sortedArr.slice(0,k).map(([key,value]) => key);

};

console.log(topKFrequent([1,1,1,2,2,3],2))
