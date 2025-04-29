/*var findMin = function (nums) {
  while (nums.length !== 1) {
    if (nums[0] > nums[nums.length - 1]) {
      // 앞에서 하나씩 자르기
      nums = nums.slice(1, nums.length);
    } else {
      return nums[0];
    }
  }
  return nums[0];
};*/
/**
 * 위의 풀이처럼 풀면 최악의 경우 O(n)이 되어버림. 양 끝을 포인터로 가리키면서 이진탐색
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
  let left = 0;
  let right = nums.length - 1;

  while (left < right) {
    let mid = Math.floor((left + right) / 2);
    if (nums[mid] > nums[right]) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }

  return nums[left];
};
