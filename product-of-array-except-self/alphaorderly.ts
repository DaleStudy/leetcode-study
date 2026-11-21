/**
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(1)
 */
function productExceptSelf(nums: number[]): number[] {
    const ans = []
    ans[0] = 1

    let acc = 1;
    for (let i = 1; i < nums.length;i += 1) {
        acc *= nums[i - 1];
        ans[i] = acc
    }

    acc = 1;
    for (let i = nums.length - 2; i >= 0; i -= 1) {
        acc *= nums[i + 1];
        ans[i] *= acc
    }

    return ans
};
