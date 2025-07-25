/**
 * 시간 복잡도: O(n log n)
 * 공간 복잡도: O(n)
 *
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    // 예외
    if (nums.length === 0) {
        return 0;
    }

    const sortedArr = [...new Set(nums)].sort((a, b) => a - b);

    let result = 1;
    let consecutive = 1;

    for (let i = 0; i < sortedArr.length - 1; i++) {
        const curr = sortedArr[i];
        const next = sortedArr[i + 1];

        if (next === curr + 1) {
            consecutive += 1;
        } else {
            consecutive = 1;
        }

        result = Math.max(result, consecutive);
    }

    return result;
};
