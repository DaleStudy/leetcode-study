/**
 * 주어진 배열에서 인접한 집을 털지 않고 훔칠 수 있는 최대 금액을 계산하는 함수
 * - 시간 복잡도: O(n)
 *   - 배열을 한 번 순회하면서 최대 금액을 계산
 * - 공간 복잡도: O(1)
 *   - 추가 배열 없이 변수만 사용하여 공간 효율성을 최적화
 * 
 * @param {number[]} nums - 각 집에 있는 돈의 양을 나타내는 배열
 * @returns {number} - 경보를 울리지 않고 훔칠 수 있는 최대 금액
 */
function rob(nums: number[]): number {
    if (nums.length === 0) return 0; // 빈 배열 처리
    if (nums.length === 1) return nums[0]; // 집이 한 채만 있는 경우, 그 집의 돈 반환

    // 1. 변수 초기화: 이전 두 집까지의 최대 금액
    let prev2 = 0; // 두 번째 이전 집까지의 최대 금액
    let prev1 = nums[0]; // 첫 번째 이전 집까지의 최대 금액

    // 2. 배열 순회: 각 집에서 훔칠 수 있는 최대 금액 계산
    for (let i = 1; i < nums.length; i++) {
        // 현재 집까지의 최대 금액은 (현재 집 + prev2) 또는 prev1 중 더 큰 값
        const cur = Math.max(nums[i] + prev2, prev1);

        // 이전 두 집의 최대 금액 업데이트
        prev2 = prev1;
        prev1 = cur;
    }

    return prev1; // 마지막 집까지의 최대 금액 반환
}