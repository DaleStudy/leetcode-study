/**
 *
 * 시간 복잡도: O(n log n) + O(n^2) => O(n^2)
 * 공간 복잡도: O(1)
 * - 자바스크립트 배열은 원래의 배열 자체를 바꿈
 */
const threeSum = (numbers) => {
  let result = [];
  numbers.sort((a, b) => a - b);

  for (let i = 0; i < numbers.length; i += 1) {
    if (i > 0 && numbers[i] === numbers[i - 1]) continue;

    let l = i + 1;
    let r = numbers.length - 1;

    while (l < r) {
      const threeSum = numbers[i] + numbers[l] + numbers[r];

      if (threeSum > 0) {
        r -= 1;
      } else if (threeSum < 0) {
        l += 1;
      } else {
        result.push([numbers[i], numbers[l], numbers[r]]);
        while (l < r && numbers[l] === numbers[l + 1]) l += 1;
        while (l < r && numbers[r] === numbers[r - 1]) r -= 1;
        l += 1;
        r -= 1;
      }
    }
  }

  return result;
};
