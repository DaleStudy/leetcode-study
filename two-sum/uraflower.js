/**
 * 주어진 배열 중 두 숫자의 합이 타겟일 때, 두 숫자의 인덱스를 반환하는 함수
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = function (nums, target) {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    const diff = target - nums[i];
    if (map.has(diff)) {
      return [map.get(diff), i];
    }
    map.set(nums[i], i);
  }
};

// 시간복잡도: O(n)
// 공간복잡도: O(n)
