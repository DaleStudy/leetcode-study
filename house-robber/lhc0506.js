/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (nums.length < 2) {
        return Math.max(nums);
    }

    let twoBefore = 0;
    let oneBefore = 0;

    nums.forEach(num => {
        const prevOneBefore = oneBefore
        oneBefore = Math.max(prevOneBefore, twoBefore + num);
        twoBefore = prevOneBefore;
    });

    return Math.max(oneBefore, twoBefore);
};
