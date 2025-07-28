/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  // 문제를 보자마자 든 생각: dfs처럼 하나씩,두개씩 가지뻗어가면서? -> 점화식,피보나치처럼 최적화된 형태겠는데? 여기까지는 생각. 근데 2칸전, 1칸전의 덧셈이라는 결론까지 내지는 못함

  // 그래서 default값을 n=1,2,3까지 세팅해놓고 생각했었다. 다른사람의 점화식 풀이 참고 후 역순으로 출발해서 2칸전, 1칸전에 대한 상황에 집중하는 방식 이해 완료. 구현은 내가 직접.
  if (n === 1) {
    return 1;
  }

  if (n === 2) {
    return 2;
  }

  return climbStairs(n - 1) + climbStairs(n - 2);
};

// 시간복잡도: O(2^n)
// 공간복잡도: O(n)

/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  const dp = Array(n).fill(0);
  dp[1] = 1;
  dp[2] = 2;

  if (n >= 3) {
    for (let i = 3; i <= n; i++) {
      dp[i] = dp[i - 1] + dp[i - 2];
    }
  }

  return dp[n];
};

// 시간복잡도: O(n)
// 공간복잡도: O(n) !! dp라는 배열대신 변수 두개로 O(1)로 줄일 수 있음
