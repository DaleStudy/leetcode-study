/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    if(nums.length === 0) return 0
    let set = new Set();
    for(const n of nums) {
        set.add(n);
    }
    let max = 0;
    for(let n of set) {
        if(!set.has(n-1)) {
            let count = 0;
            while(set.has(n++)) {
                count++;
            }
            max = Math.max(max, count);
        }
    }
    return max;
};

/* Test code */
console.log(longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6])); // true
