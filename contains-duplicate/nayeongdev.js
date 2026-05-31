/**
 * @param {number[]} nums
 * @return {boolean}
 * O(nlog(n)) : 정렬 O(nlog(n)) + 탐색 O(n)
 */
var containsDuplicate = function (nums) {
    const sortedNums = nums.toSorted((a, b) => a - b)
    for (let i = 0; i < nums.length - 1; i++) {
        if (sortedNums[i] === sortedNums[i + 1]) {
            return true
        }
    }
    return false
};
