/**
 * 시간 복잡도:
 *   메모이제이션을 사용하여 n까지 가기 위한 방법의 수를 저장.
 *   재귀 함수는 최대 n만큼 호출됨.
 *   따라서, 시간 복잡도는 O(n)
 * 공간 복잡도:
 *   메모 객체의 크기는 n의 크기와 같음.
 *   재귀 함수는 최대 n만큼 호출됨.
 *   따라서, 공간 복잡도는 O(n)
 */
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
  const memo = { 1:1, 2:2 };
  const recurse = (n) => {
      if(memo[n]) {
          return memo[n];
      }
      memo[n] = recurse(n - 1) + recurse(n - 2);
      return memo[n];
  }
  return recurse(n);
};
