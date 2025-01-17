/**
 * 본인 인덱스에 있는 값을 제외한 모든 수의 곱
 * 알고리즘 복잡도
 * - 시간복잡도: O(n)
 * - 공간복잡도: O(1)
 * @param nums
 */
function productExceptSelf(nums: number[]): number[] {
    let len = nums.length
    let output = Array(len).fill(1)

    /* ex) [1, 2, 3, 4]
    left >>>
    i = 0 -> 1 = 1
    i = 1 -> 1 * 1 = 1
    i = 2 -> 1 * 1 * 2 = 2
    i = 3 -> 1 * 1 * 2 * 3 = 6
     */
    // 왼쪽부터 누적 곱
    let left = 1
    for (let i = 0; i < len; i++) {
        output[i] *= left
        left *= nums[i]
    }

    /*
    right >>>
    i = 3 -> 1 = 1
    i = 2 -> 1 * 4 = 4
    i = 1 -> 1 * 4 * 3 = 12
    i = 3 -> 1 * 4 * 3 * 2 = 24

    output >>>
    i = 0 -> 1 * 24 = 24
    i = 1 -> 1 * 12 = 12
    i = 2 -> 2 * 4= 8
    i = 3 -> 6 * 1 = 6
     */
    // 오른쪽부터 누적 곱을 output 각 자리에 곱함
    let right = 1
    for (let i = len - 1; i >= 0; i--) {
        output[i] *= right
        right *= nums[i]
    }

    return output
}
