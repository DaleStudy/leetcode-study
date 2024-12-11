/**
 * @param {number[]} nums
 * @return {boolean}

 nums 배열내의 아무 정수나 2개 이상 중복되면 true를 반복하는 함수.

 시간 복잡도: O(n)
 */
var containsDuplicate = function (nums) {
  return nums.length !== new Set(nums).size
}

console.log(containsDuplicate([1, 2, 3, 1])); // true
// console.log(containsDuplicate([1, 2, 3, 4])); // false
// console.log(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])); // true