/**
 * @param {number} n
 * @return {number[]}
 */

/**
 * Runtime: 82ms, Memory: 57.03MB
 *
 * Time complexity: O(logN < N+1 ? N+1 : logN 단,보통의 경우 N+1)
 * Space complexity: O(N+1)
 *
 * Note: necessary to think of an alternative approach
 * **/

function decimalToBinary(decimal) {
  let binaryBitCount = 0;

  while (decimal > 1) {
    binaryBitCount += decimal % 2 === 1 ? 1 : 0;
    decimal = Math.floor(decimal / 2);
  }
  binaryBitCount += decimal === 1 ? 1 : 0;

  return binaryBitCount;
}
var countBits = function (n) {
  const answer = [];

  for (let i = 0; i < n + 1; i++) {
    answer.push(decimalToBinary(i));
  }

  return answer;
};

/**
 * 인상 깊었던 풀이
 *
 * Runtime : 60ms
 *
 * 비트 연산의 속성과 dp를 활용해 푼 풀이
 *
 * [간단설명]
 * 4일때 100이고, 5일때 101, 6일때 110이다.
 * 이때 4를 2진수로 표현한 100이 가진 1의 개수를 활용해 5,6의 1의 개수를 찾는 것이다.
 * 100에서 1을 더한 101이나, 110은 100의 1의 개수인 1개에서 1을 더한 2개가 된다.
 * result[5 & 4] => 비트 연산을 통해 100과 101의 비트 앤드 연산을 해서 100이 되고, 이는 101의 가장 오른쪽 1을 제거한 값이 된다.
 * result[6 & 5] => 비트 연산을 통해 110과 101의 비트 앤드 연산을 해서 100이 되고, 이는 110의 가장 오른쪽 1을 제거한 값이 된다.
 * 이진수는 1씩 더하기 때문에 나보다 하나 큰 수와 앤드 연산을 하면 작은 수가 0으로 끝나면 큰 수는 1로 끝나고,
 * 작은 수가 1로 끝나면 큰 수는 0으로 끝나기 대문에 이런 속성을 갖는다.
 *
 *
 */

var countBits = function (n) {
  let result = new Array(n + 1).fill(0);
  for (let i = 1; i <= n; i++) {
    result[i] = result[i & (i - 1)] + 1;
  }
  return result;
};
