/**
 * 시간복잡도: O(n²)
 * 공간복잡도: O(1) (결과 배열 제외)
 * 풀이 방법: 정렬 후 투 포인터 방식
 * @param {number[]} nums
 * @return {number[][]}
 */
const threeSum = function (nums) {
  const sortedNums = nums.sort((a, b) => a - b);
  const result = [];

  for (let i = 0; i < sortedNums.length; i += 1) {
    // 첫 번째 요소의 중복 제거
    if (i > 0 && sortedNums[i] === sortedNums[i - 1]) {
      continue;
    }

    let left = i + 1;
    let right = sortedNums.length - 1;

    while (left < right) {
      const threeSum = sortedNums[i] + sortedNums[left] + sortedNums[right];

      if (threeSum > 0) {
        right -= 1;
      } else if (threeSum < 0) {
        left += 1;
      } else {
        result.push([sortedNums[i], sortedNums[left], sortedNums[right]]);

        // 중복 제거
        while (left < right && sortedNums[left] === sortedNums[left + 1]) {
          left += 1;
        }
        while (left < right && sortedNums[right] === sortedNums[right - 1]) {
          right -= 1;
        }

        left += 1;
        right -= 1;
      }
    }
  }

  return result;
};
