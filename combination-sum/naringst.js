/**
 * NOTE:
 * 1. dp를 사용하려고 했으나 시간초과
 * 2. 재귀를 활용해 가능한 한 모든 중복조합을 구해서 계산하기
 *
 */

// 1번 시도

var combinationSum = function (candidates, target) {
  const dp = Array(target + 1).fill(1);

  for (let i = 2; i < candidates.length; i++) {
    dp[i] = 1;
    for (let j = 1 < Math.floor(i / 2); ; j++) {
      dp[i] += dp[j] * dp[i - j];
    }
    // ...이미 시간초과
  }
};

// 2번 풀이(참고)
// 재귀를 활용해 한 값이 중복으로 더해지는 부분을 처리 -> target보다 클때까지 재귀
// for 문을 활용해 candidates의 모든 값을 순회
//
/**
 * Runtime: 78ms, Memory: 59.13MB
 * Time complexity: O(n * target/n) => O(2^n * k) by gpt (k: 조합의 길이)
 * Space complexity: O(n * target/n)  => O(target) + O(2^n * k ) by gpt
 *
 */

var combinationSum = function (candidates, target) {
  const result = [];

  function permute(arr = [], sum = 0, idx = 0) {
    // target보다 합이 크면 리턴
    if (sum > target) return;
    // 같은 경우에만 result에 담기
    if (sum === target) result.push(arr);

    for (let i = idx; i < candidates.length; i++) {
      // target보다 합이 작으면 재귀적으로 해당 값을 arr에 넣고, sum에 추가
      permute([...arr, candidates[i]], sum + candidates[i], i);
    }
  }
  permute();
  return result;
};
