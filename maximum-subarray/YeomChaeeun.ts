/**
 * 연속되는 서브 배열로 최대 합을 구하기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n)
 * - 공간 복잡도: O(1)
 * @param nums
 */
function maxSubArray(nums: number[]): number {
    if(nums.length === 1) return nums[0]

    let currentSum = nums[0]
    let maxSum = nums[0]
    for(let i = 1; i < nums.length; i++) {
        currentSum = Math.max(nums[i], currentSum + nums[i])
        // 최대값 갱신
        maxSum = Math.max(maxSum, currentSum)
    }

    return maxSum
}
