/**
* 본인을 기준으로 좌측과, 우측 나눠서 곱한다.
* 담아놓을 변수를 놓고 진행한다.
 * @param {number[]} nums
 * @return {number[]}
 *
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(n)
 */
var productExceptSelf = function(nums) {
    const n = nums.length;
    const left = Array(n).fill(1);
    const right = Array(n).fill(1);
    const res = Array(n);

    // 좌측 곱
    for (let i = 1; i < n; i++) {
        left[i] = nums[i - 1] * left[i - 1];
    }

    // 우측 곱
    for (let i = n - 2; i >= 0; i--) {
        right[i] = nums[i + 1] * right[i + 1];
    }

    for (let i = 0; i < n; i++) {
        res[i] = left[i] * right[i];
    }

    return res;
};
