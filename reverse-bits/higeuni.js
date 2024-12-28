/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 * 
 * Time Complexity: O(n)? n이 32이기 때문에 O(1)? 
 * Space Complexity: O(1)
 */

// 일반적인 풀이
var reverseBits = function(n) {
  const binary = n.toString(2);
  const reversedBinary = binary.split('').reverse().join('').padEnd(32, '0');
  const answer = parseInt(reversedBinary, 2);

  return answer;
  // return parseInt(n.toString(2).split('').reverse().join('').padEnd(32, '0'), 2);
};

/**
 * 
 * Time Complexity: O(1)
 * Space Complexity: O(1)
*/

// 비트 연산을 이용한 풀이
var reverseBits2 = function(n) {
  let result = 0;
  for(let i = 0; i < 32; i++) {
    // result를 왼쪽으로 시프트하고 n의 마지막 비트를 더함
    result = (result << 1) | (n & 1);
    // n을 오른쪽으로 시프트
    n = n >> 1;
  }
  return result >>> 0;
}

