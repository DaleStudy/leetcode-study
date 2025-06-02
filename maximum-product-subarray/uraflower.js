/**
 * 주어진 배열에서 가장 큰 부분 배열의 곱을 반환하는 함수
 * @param {number[]} nums
 * @return {number}
 */
const maxProduct = function (nums) {
    let min = nums[0];
    let max = nums[0];
    let result = nums[0]; // 현재까지 가장 큰 부분 배열 곱을 저장

    for (let i = 1; i < nums.length; i++) {
        let tempMin = Math.min(nums[i], min * nums[i], max * nums[i]);
        let tempMax = Math.max(nums[i], min * nums[i], max * nums[i]);
        min = tempMin;
        max = tempMax;
        result = Math.max(result, max);
    }

    return result;
}

// 시간복잡도: O(n)
// 공간복잡도: O(1)
