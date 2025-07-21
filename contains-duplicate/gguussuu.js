/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    //Set은 중복된 값을 허용하지 않기 때문에, 배열을 Set으로 변환한 후 길이를 비교하여 중복 여부를 확인
    const hasDuplicate = new Set(nums).size !== nums.length;
    return hasDuplicate;
};