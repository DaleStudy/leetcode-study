/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let dict = new Map();

    for(const [index, num] of nums.entries()){
        if(dict.has(target-num) && dict.get(target-num) != index){
            return [dict.get(target-num),index];
        }
        dict.set(num, index);
    }
};
