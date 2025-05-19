/**
 * @param {number} n
 * @return {number}
 */
//1. divide the number by 2 and count the remainder
var hammingWeight = function (n) {
  let count = 0;
  while (n > 0) {
    if (n % 2 === 1) {
      count++;
    }
    n = Math.floor(n / 2);
  }
  return count;
};

//2. Count the number of set bits (1s) in the binary representation of n
var hammingWeight = function (n) {
  return n.toString(2).split("1").length - 1;
};

//3. bit manipulation
var hammingWeight = function (n) {
  let count = 0;
  while (n > 0) {
    count += n & 1; // 마지막 비트가 1이면 count++
    n = n >>> 1; // 오른쪽으로 한 비트 이동 (2로 나눔)
  }
  return count;
};
