/**
 * @param {number[]} nums
 * @return {number[][]}
 *
 * 1. 투포인터를 사용하기 위해 정렬
 * 2. 투포인터를 사용하여 합이 0인 경우 추가
 * 3. 중복 된 값 스킵
 *
 * 시간 복잡도: O(n^2)
 * 공간 복잡도: O(K + kLogK) (K: 결과 배열의 크기, kLogK: 정렬 공간)
 */
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    const arr = [];

    // 투포인터를 사용하기 위해 정렬
    nums.sort((a, b) => a - b);

    for (let i = 0; i < nums.length - 2; i++) {
        // 중복 된 값 스킵
        if (i > 0 && nums[i] ===  nums[i - 1]) continue;

        let left = i + 1;
        let right = nums.length - 1;

        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];

            if (sum === 0) {
                arr.push([nums[i], nums[left], nums[right]]);

                // 중복 된 값 스킵
                while (left < right && nums[left] === nums[left + 1]) left++;
                while (left < right && nums[right] === nums[right - 1]) right--;

                left++;
                right--;
            } else if (sum > 0) {
                right--;
            } else {
                left++;
            }
        }
    }

    return arr;
};