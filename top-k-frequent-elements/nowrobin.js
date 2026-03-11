/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

// 13ms 60mb
var topKFrequent = function(nums, k) {
    let freq = new Map()
    for(let i of nums){
        freq.set(i, (freq.get(i)|| 0) + 1 )
    }
    const sorted = [...freq.entries()].sort((a, b) => b[1] - a[1]);
    let result = []
    for (let j =0 ; j< k ; j++){
        result.push(sorted[j][0])
    } 
    return result
};
