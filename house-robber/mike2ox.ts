/**
 * Source: https://leetcode.com/problems/house-robber/
 * 요점: 인접한 집을 방문하지 않고 훔칠 수 있는 최대 금액을 계산
 * 풀이 시간: 40분
 * 풀이방법: DP를 사용하여 최적의 해결책을 구함
 * 시간복잡도: O(n) - 배열을 한 번만 순회
 * 공간복잡도: O(1) - 상수 공간만 사용 (최적화 후)
 */
function rob(nums: number[]): number {
  // 엣지 케이스 처리
  const n = nums.length;
  if (n === 0) return 0;
  if (n === 1) return nums[0];

  // 공간 최적화: 전체 dp 배열 대신 두 개의 변수만 사용
  let prevTwo = nums[0]; // dp[i-2]
  let prevOne = Math.max(nums[0], nums[1]); // dp[i-1]

  // i=2부터 시작하여 최적의 값 계산
  for (let i = 2; i < n; i++) {
    const current = Math.max(
      prevOne, // 현재 집을 건너뛰는 경우
      prevTwo + nums[i] // 현재 집을 털고 i-2 위치까지의 최적해를 더하는 경우
    );

    // 다음 반복을 위해 값 업데이트
    prevTwo = prevOne;
    prevOne = current;
  }

  return prevOne;
}
