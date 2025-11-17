/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const numsMap = new Map();

    for(const num of nums){
        const currentNums = numsMap.get(num);

        if(!currentNums){
            numsMap.set(num, 1);
            continue;
        }

        numsMap.set(num, currentNums + 1)
    }

    const sortedNums = [...numsMap].sort((a,b) => b[1] - a[1]);

    const frequencyNums = sortedNums.map(([num])=> num);

    return frequencyNums.slice(0,k);
};
