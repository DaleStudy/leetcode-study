/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    var dict = {};
    var sortTable = [];
    for(let i = 0; i < nums.length; i ++) {
        dict[nums[i]] = dict[nums[i]] ? dict[nums[i]] + 1 : 1;
    }
    
    for(let ele in dict) {
        sortTable.push([ele, dict[ele]]);
    }
    sortTable.sort((a, b) => {
        return b[1] - a[1];
    });

    return sortTable.slice(0, k).map(e => Number(e[0]))
};
