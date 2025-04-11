/*
* 투 포인터 방식 사용
* 시간 복잡도: O(n^2)
* 공간 복잡도; O(n^2)
*/

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
const threeSum = (nums) => {
  const sorted = [...nums].sort((a, b) => a - b);
  const results = [];

  sorted.forEach((val, i) => {
    if (i > 0 && val === sorted[i - 1]) return;

    let left = i + 1;
    let right = sorted.length - 1;

    while (left < right) {
      const sum = val + sorted[left] + sorted[right];

      if (sum === 0) {
        results.push([val, sorted[left], sorted[right]]);

        // 중복된 left/right 스킵
        const currentLeft = sorted[left];
        const currentRight = sorted[right];

        while (left < right && sorted[left] === currentLeft) left++;
        while (left < right && sorted[right] === currentRight) right--;
      } else if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
  });

  return results;
};
