/**
 * 한 칸 또는 두 칸씩 n개의 계단을 오르는 방법의 가짓수를 반환하는 함수
 * @param {number} n
 * @return {number}
 */
const climbStairs = function(n) {
  const steps = Array.from({length: n + 1}).fill(0);

  for (let i = 1; i <= n; i++) {
    if (i === 1) {
      steps[i] = 1;
    } else if (i === 2) {
      steps[i] = 2;
    } else {
      steps[i] = steps[i-1] + steps[i-2];
    }
  }

  return steps[n];
};

// 시간복잡도: O(n)
// 공간복잡도: O(n)
