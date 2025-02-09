/**
 * 최대 부분 곱 구하기
 * 알고리즘 복잡도
 *  - 시간 복잡도: O(n)
 *  - 공간 복잡도: O(1)
 * @param nums
 */
function maxProduct(nums: number[]): number {
    if(nums.length === 1) return nums[0]

    let max = nums[0]
    let currMax = nums[0]
    let currMin = nums[0]

    for(let i = 1; i < nums.length; i++) {
        const temp = currMax;

        currMax = Math.max(
            nums[i], temp * nums[i], currMin * nums[i]
        )

        currMin = Math.min(
            nums[i], temp * nums[i], currMin * nums[i]
        )

        max = Math.max(max, currMax);
    }

    return max;

}
