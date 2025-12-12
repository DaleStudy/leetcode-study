/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const numsSet = new Set(nums);


    if(nums.length === 0) return 0

    const sortedNums = [...numsSet].sort((a,b) => a-b);

    const results = [];

    let result = 1;

    for(let i = 0; i < sortedNums.length-1; i++){
        const current = sortedNums[i];
        const next = sortedNums[i+1];

        if((current + 1) === next){
            result += 1;
        }else{
            results.push(result);
            result = 1;
        }
    }

    results.push(result);


    return Math.max(...results)
};
