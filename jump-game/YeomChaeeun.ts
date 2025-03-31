/**
 * 점프 게임 현재 인덱스에서 인덱스 값만큼 점프하여 마지막 인덱스까지 도달할 수 있는지 구하기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n2)
 * - 공간 복잡도: O(n)
 * @param nums
 */
function canJump(nums: number[]): boolean {
    const dp = new Array(nums.length).fill(false)

    dp[0] = true
    for(let i = 0; i < nums.length; i++) {
        if(!dp[i]) continue;

        for(let step = 1; step <= nums[i]; step++) {
            if(i + step < nums.length) {
                dp[i + step] = true;
            }
        }

        if(dp[nums.length -1]) {
            return true;
        }
    }

    return dp[nums.length - 1];
}
