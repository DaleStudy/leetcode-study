/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (nums.length === 1) return nums[0];

    const helper = (snums) => {
        let rob1 = 0,
            rob2 = 0;

        for (let n of snums) {
            const newRob = Math.max(rob1 + n, rob2);
            rob1 = rob2;
            rob2 = newRob;
        }

        return rob2;
    };

    return Math.max(helper(nums.slice(1)), helper(nums.slice(0, -1)));
};

