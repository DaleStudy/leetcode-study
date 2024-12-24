/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
      if (i !== j) {
        if (nums[i] + nums[j] === target) {
          return [i, j];
        }
      }
    }
  }
};

// 처음에 풀었던 방법 -> 시간 복잡도가 O(n^2)로 nums 배열에 있는 값이 늘어날수록 성능상 좋지 못함
// 시간 복잡도: O(n^2)
// 공간 복잡도: O(1)

// 두 번째 푼 방법 -> 이전에 threeSum 문제 풀 때 정렬 + 포인터 이용한 것처럼 이 문제도 그런식으로 품
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const numsIndex = nums.map((num, i) => ({ num, i })); // 원래 인덱스 저장
  //console.log(numsIndex);

  numsIndex.sort((a, b) => a.num - b.num); // 오름차순 정렬
  //console.log(numsIndex);

  // left와 right 포인터 이용해 target값과 동일한 것 찾기
  let left = 0;
  let right = numsIndex.length - 1;

  while (left < right) {
    const sum = numsIndex[left].num + numsIndex[right].num;

    if (sum > target) {
      right--;
    } else if (sum < target) {
      left++;
    } else {
      return [numsIndex[left].i, numsIndex[right].i];
    }
  }
  return null;
};

// 첫 번째 푼 방법보다 공간 복잡도가 늘어났지만 시간 복잡도는 줄어듦
// 시간 복잡도: O(n log n)
// 공간 복잡도: O(n)
