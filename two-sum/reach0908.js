/**
 * @description
 * time complexity: O(n^2)
 * space complexity: O(1)
 * 풀이 방법:
 * 카운터를 통해 반복문 돌기
 * 겉으로는 반복문이 한개 같아보이지만 이중반복문이다.
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSumSoluton1 = function (nums, target) {
  let left = 0;
  let right = 1;
  while (left < nums.length - 1) {
    const sum = nums[left] + nums[right];
    if (sum === target) {
      return [left, right];
    }

    if (right < nums.length - 1) {
      right += 1;
    } else {
      left += 1;
      right = left + 1;
    }
  }
};

/**
 * @description
 * 다른 사람들의 풀이를 보고 개선한 솔루션
 * time complexity: O(n)
 * space complexity: O(n)
 * 풀이 방법:
 * 이전 값들 중에 원하는 값이 있는지만 확인 후 추출, 시간복잡도를 크게 감소시킴
 * 하지만 해쉬맵을 만들어야해서 공간복잡도는 O(n)으로 변경
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSumSoluton2 = function (nums, target) {
  const hashMap = new Map();

  for (let i = 0; i < nums.length; i += 1) {
    const calculatedTarget = target - nums[i];
    if (hashMap.has(calculatedTarget)) {
      return [i, hashMap.get(calculatedTarget)];
    }

    hashMap.set(nums[i], i);
  }

  return [];
};
