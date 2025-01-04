/**
 * 주어진 배열의 중간에 없는 숫자 찾기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(nlogn)
 * - 공간 복잡도: O(1)
 * @param nums
 */
function missingNumber(nums: number[]): number {
    if(nums.length === 1) {
        return nums[0] === 0 ? 1 : 0
    }

    nums.sort((a, b) => a - b)

    for(let i = 0; i < nums.length; i++) {
        if(nums[0] !== 0) return 0
        if(nums[i] + 1 !== nums[i + 1])
            return nums[i] + 1
    }
}
