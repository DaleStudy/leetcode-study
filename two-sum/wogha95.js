// 2차: index를 값으로 갖는 Map을 활용하여 한번의 순회로 답안 도출
// TC: O(N)
// SC: O(N)

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const valueIndexMap = new Map();

  for (let index = 0; index < nums.length; index++) {
    const value = nums[index];
    const anotherValue = target - value;

    if (valueIndexMap.has(anotherValue)) {
      return [index, valueIndexMap.get(anotherValue)];
    }

    valueIndexMap.set(value, index);
  }
};

// 1차: 정렬 후 투포인터 활용
// TC: O(N * logN)
// SC: O(N)

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const sortedNums = nums
    .map((value, index) => ({ value, index }))
    .sort((a, b) => a.value - b.value);
  let left = 0;
  let right = sortedNums.length - 1;

  while (left < right) {
    const sum = sortedNums[left].value + sortedNums[right].value;
    if (sum < target) {
      left += 1;
    } else if (sum > target) {
      right -= 1;
    } else {
      return [sortedNums[left].index, sortedNums[right].index];
    }
  }
};
