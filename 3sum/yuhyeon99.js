/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    var answer = new Set();
    nums.sort((a, b) => a - b);

    for(let i = 0; i < nums.length - 2; i ++) {
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        let usedNumSet = new Set();
        for(let j = i + 1; j < nums.length; j ++) {
            let target = -(nums[i] + nums[j]);

            if(usedNumSet.has(target)) {
                let triplets = [nums[i], nums[j], target].sort((a, b) => a - b);
                answer.add(triplets.join(','));
            }

            usedNumSet.add(nums[j]);
        }
    }

    return [...answer].map(e => e.split(',').map(Number));
};
