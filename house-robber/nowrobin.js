/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    // 집의 개수
    const n = nums.length;

    // 집이 하나뿐이면 그 집을 터는 것이 최대값
    if (n === 1) {
        return nums[0];
    }

    // dp[i] = 0번 집부터 i번 집까지 고려했을 때 훔칠 수 있는 최대 금액
    const dp = Array(n).fill(0);

    // 첫 번째 집까지의 최대 금액
    dp[0] = nums[0];

    // 두 번째 집까지의 최대 금액
    // 두 집은 동시에 털 수 없으므로 둘 중 큰 값을 선택
    dp[1] = Math.max(nums[0], nums[1]);

    // 세 번째 집부터 마지막 집까지 반복
    for (let i = 2; i < n; i++) {

        // 두 가지 선택지 중 더 큰 값을 선택
        // 1️⃣ 현재 집을 털지 않는다 → 이전 집까지의 최대 금액(dp[i-1])
        // 2️⃣ 현재 집을 턴다 → 전전 집까지의 최대 금액(dp[i-2]) + 현재 집 돈(nums[i])
        dp[i] = Math.max(dp[i - 1], nums[i] + dp[i - 2]);
    }

    // 마지막 집까지 고려했을 때의 최대 금액 반환
    return dp[n - 1];    
};
