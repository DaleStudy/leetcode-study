/**
 * 3차 (시간, 공간 복잡도 개선)
 * 동일한 down방향, right방향들 중에서 나열하는 방법
 * 즉, ((m - 1) + (n - 1))! / ((m - 1)! * (n - 1)!)
 * (+ 팩토리얼의 수는 매우 빠르게 커지므로 중간 나눗셈이 가능할때마다 나누어서 integer 범위를 넘지 않도록 방지)
 *
 * TC: O(M + N)
 * 1부터 최대 (M - 1) + (N - 1)까지 순회
 *
 * SC: O(1)
 * 계산의 결과 변수가 m, n과 무관하므로 상수의 공간복잡도
 */

/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function (m, n) {
  // 1. down방향, right방향의 수
  const NUMBER_OF_DOWN = m - 1;
  const NUMBER_OF_RIGHT = n - 1;

  // 2. factorial 계산을 위한 변수
  let result = 1;
  let factorialOfDown = 1;
  let factorialOfRight = 1;

  // 3. 'down방향 수 + right방향 수'만큼 순회하면서
  for (let number = 1; number <= NUMBER_OF_DOWN + NUMBER_OF_RIGHT; number++) {
    result *= number;

    // 4. factorial 값들이 커지지 않도록 나눌수 있을때마다 나눔 (factorial of down)
    if (number <= NUMBER_OF_DOWN) {
      factorialOfDown *= number;
      if (result % factorialOfDown === 0) {
        result /= factorialOfDown;
        factorialOfDown = 1;
      }
    }

    // 5. factorial 값들이 커지지 않도록 나눌수 있을때마다 나눔 (factorial of right)
    if (number <= NUMBER_OF_RIGHT) {
      factorialOfRight *= number;
      if (result % factorialOfRight === 0) {
        result /= factorialOfRight;
        factorialOfRight = 1;
      }
    }
  }

  return result / factorialOfDown / factorialOfRight;
};

/**
 * 2차 (공간복잡도 개선)
 * 이전 풀이에서 모든 행의 경로수를 기억할 필요가 없는 점을 활용
 *
 * TC: O(M * N)
 * 경로 수를 기록하기 위한 N배열 순회 * (M - 1)
 *
 * SC: O(N)
 * 경로수 기록을 위한 1차원 배열
 */

/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function (m, n) {
  // 1. 최상단의 경로수는 모두 1
  const numberOfPaths = new Array(n).fill(1);

  for (let row = 1; row < m; row++) {
    // 2. 각 좌표의 경로수는 현좌표(1차 풀이의 row-1)와 좌측좌표(1차 풀이의 column-1)의 합
    for (let column = 1; column < n; column++) {
      numberOfPaths[column] += numberOfPaths[column - 1];
    }
  }

  return numberOfPaths[n - 1];
};

/**
 * 1차
 * 각 좌표의 경로수를 기록하여 dp로 풀이
 * 현좌표까지의 경로수 = 상단좌표에서 온 경우 + 좌측좌표에서 온 경우
 * dp[row][column] = dp[row - 1][column] + dp[row][column - 1]
 *
 *
 * TC: O(M * N)
 * 경로수를 기록한 2차원 배열을 전체 순회
 *
 * SC: O(M * N)
 * 경로수 기록을 위한 2차원 배열
 */

/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function (m, n) {
  // 1. 각 좌료까지의 경로수를 기록하기 위한 배열
  const numberOfPaths = new Array(m).fill(new Array(n).fill(0));

  // 2. 최좌측에 있는 좌표의 경로수는 1
  for (let row = 0; row < m; row++) {
    numberOfPaths[row][0] = 1;
  }

  // 3. 최상단에 있는 좌표의 경로수는 1
  for (let column = 0; column < n; column++) {
    numberOfPaths[0][column] = 1;
  }

  // 4. 그 외 각 좌표는 바로 위 좌표(column-1)와 바로 왼쪽 좌표(row-1)의 경로수의 합
  for (let row = 1; row < m; row++) {
    for (let column = 1; column < n; column++) {
      numberOfPaths[row][column] =
        numberOfPaths[row - 1][column] + numberOfPaths[row][column - 1];
    }
  }

  return numberOfPaths[m - 1][n - 1];
};
