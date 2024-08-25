/**
 * @param {number} n
 * @return {number}
 */
let hammingWeight = function (n) {
  let count = 0;
  let sum = n;

  while (sum > 0) {
    // n에서 가장 오른쪽 비트가 1인 경우 count 증가
    if (sum % 2 === 1) {
      count++;
    }
    // sum을 2로 나누어서 다음 비트를 확인
    sum = Math.floor(sum / 2);
  }

  return count;
};
