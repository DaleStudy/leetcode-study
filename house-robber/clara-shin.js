/**
 * 도둑이 집을 털 때 인접한 집들은 연속으로 못 턴다
 * 각 집에 있는 돈의 양이 담긴 배열이 주어질 때, 경찰에 발각되지 않고 훔칠 수 있는 최대 금액을 구해야 한다
 * 
 * 접근 방식: 동적 프로그래밍(DP) - 각 단계마다 최적의 선택을 해야 함
 * 각 집 위치에서 두 가지 선택:
 * 1. 현재 집을 털어 (그러면 인접한 이전 집은 털지 못함)
 * 2. 현재 집을 털지 마 (이전 집까지의 최적 방법 유지)
 * 
 * dp[i] = i번째 집까지 고려했을 때 훔칠 수 있는 최대 금액
 * dp[i] = max(dp[i-2] + nums[i], dp[i-1])
 * 
 * dp[i-2] + nums[i]: 현재 집을 털고 ---> i-2번째 집까지의 최대값 더하기
 * dp[i-1]: 현재 집을 털지 않고 ---> i-1번째 집까지의 최대값 유지
 * /

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  if (nums.length === 0) return 0;
  if (nums.length === 1) return nums[0];

  // dp[i] = i번째 집까지 고려했을 때 훔칠 수 있는 최대 금액
  let dp = new Array(nums.length);
  dp[0] = nums[0];
  dp[1] = Math.max(nums[0], nums[1]);

  // 세 번째 집부터는 두 가지 선택 중 더 큰 값 선택
  // 1. 현재 집을 털고 i-2번째 집까지의 최대값 더하기
  // 2. 현재 집을 털지 않고 i-1번째 집까지의 최대값 선택
  for (let i = 2; i < nums.length; i++) {
    dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]);
  }

  // 마지막 집까지 고려한 최대 금액 리턴
  return dp[nums.length - 1];
};
