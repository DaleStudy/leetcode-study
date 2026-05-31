/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    if(!nums.length) return 0;

    nums.sort((a, b) => a - b);
    var answer = 0;
    var length = 1;
    for(let i = 0; i < nums.length - 1; i ++) {
        if(nums[i] === nums[i + 1]) {
            continue;
        } else if (nums[i] + 1 === nums[i + 1]) {
            length ++;
        } else {
            answer = Math.max(length, answer);
            length = 1;
        }
    }

    answer = Math.max(length, answer);

    return answer;
};
