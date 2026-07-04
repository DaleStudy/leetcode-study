/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

/*
TC: O(n)
SC: O(n) -> Map 사용
*/

var twoSum = function (nums, target) {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (map.has(complement)) return [map.get(complement), i];
    map.set(nums[i], i);
  }
};

/*
With two points
TC: O(nlogn) -> sort 사용
SC: O(n) -> origin index 배열 생성
*/

var twoSum = function (nums, target) {
  const numsWithOriginIndex = nums.map((num, i) => [num, i]);
  numsWithOriginIndex.sort(([a], [b]) => a - b);

  let left = 0;
  let right = nums.length - 1;
  let result;

  while (left < right) {
    const [leftValue, leftIndex] = numsWithOriginIndex[left];
    const [rightValue, rightIndex] = numsWithOriginIndex[right];
    const sum = leftValue + rightValue;

    if (sum === target) {
      result = [leftIndex, rightIndex];
      break;
    }

    if (sum > target) right--;
    else left++;
  }

  return result;
};

/*
Brute force
TC: O(n^2)
SC: O(1)
*/

var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
  return result;
};
