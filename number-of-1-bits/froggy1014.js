
// Time complexity: O(k)
// Space complexity: O(k)

/**
 * @param {number} n
 * @return {number}
 */

// 문자열 변환을 사용한 풀이 
// 이진수로 변환된 수를 문자열로 변환후 1의 개수를 세는 방법
// 문자열 변환은 비트 연산자보다 느리지만 이해하기 쉬운 방법
var hammingWeight = function (n) {
  return n.toString(2).split('').filter(b => b === '1').length
}

// Time complexity: O(1)
// Space complexity: O(1)

// 비트 연산자를 사용한 풀이
// 비트 연산자는 이진수로 변환된 수를 비교하는 연산자
// 자바스크립트 엔진이 숫자를 32비트 정수로 변환후 CPU 수준에서 연산을 수행
var hammingWeight = function (n) {
  let count = 0;
  for (let i = 0; i < 32; i++) {
    if ((n & (1 << i)) !== 0) {
      count++;
    }
  }
  return count;
};
