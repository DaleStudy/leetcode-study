/**
 * @param {number[]} nums
 * @return {boolean}
 * 
 * 접근: 중첩 반복문을 통해 중복이 있으면 true 반환, 중복이 없으면 false를 반환하도록 설계하였습니다.
 * 그러나 배열의 요소를 두 번 돌기 때문에 더 효율적인 방법으로 설계하고자 하였습니다.
 * 
 * 해결: 더 효율적인 방법으로 중복 여부를 검사하는 Set을 사용하게 되었습니다.
 * Set에 해당 요소가 있는 지 확인하고 있다면 true를 없다면 false를 반환하도록 하였습니다.
 */

var containsDuplicate = function(nums) {
    const duplicate = new Set();

    for (let i = 0; i < nums.length; i++) {
        if (duplicate.has(nums[i])) {
            return true;
        }
        duplicate.add(nums[i]);
    }

    return false;
};
