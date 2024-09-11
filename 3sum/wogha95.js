/**
 * TC: O(N^2)
 * SC: O(N)
 *
 * 풀이
 * 2sum의 확장 문제 (nums[i] == nums[j] + nums[k])
 * 2sum은 투포인터로 시간복잡도 O(N)을 만들기 위해 투포인터를 활용한다.
 */

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  const result = [];
  const sortedNums = nums.sort((a, b) => a - b);

  // 3개 항의 합이 0이 될 수 없는 경우
  if (sortedNums[0] > 0 || sortedNums[sortedNums.length - 1] < 0) {
    return [];
  }

  // 1. 순회를 하며 2sum의 target 값을 지정함
  for (let index = 0; index < sortedNums.length - 2; ) {
    twoSum(index + 1, sortedNums[index]);
    // 3. 동일한 숫자를 제외하기 위해 순회
    while (sortedNums[index] === sortedNums[index + 1]) {
      index += 1;
    }
    index += 1;
  }

  return result;

  function twoSum(startIndex, target) {
    let left = startIndex;
    let right = sortedNums.length - 1;

    // 2. 투포인터로 2sum이 target이 되는 경우를 찾기 위해 순회
    while (left < right) {
      const sum = sortedNums[left] + sortedNums[right];

      if (sum + target === 0) {
        result.push([target, sortedNums[left], sortedNums[right]]);
      }

      if (sum + target < 0) {
        while (sortedNums[left] === sortedNums[left + 1]) {
          left += 1;
        }
        left += 1;
      } else {
        while (sortedNums[right] === sortedNums[right - 1]) {
          right -= 1;
        }
        right -= 1;
      }
    }
  }
};
