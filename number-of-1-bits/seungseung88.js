/**
 * 시간 복잡도: O(log n)
 * 공간 복잡도: O(n)
 */
//
var hammingWeight = function (n) {
  let count = 0;

  while (n > 0) {
    if (n % 2) count += 1;

    // Math.floor랑 같은 역할
    n = ~~(n / 2);
  }

  return count;
};

// 비트 연산자 사용
var hammingWeight = function (n) {
  let count = 0;
  while (num > 0) {
    if (n & 1) count += 1;
    n >>>= 1;
  }

  return countOne;
};
