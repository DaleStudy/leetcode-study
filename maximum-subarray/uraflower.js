/**
 * 주어진 배열에서 원소의 합이 가장 큰 부분 배열의 합을 반환하는 함수
 * @param {number[]} nums
 * @return {number}
 */
const maxSubArray = function(nums) {
    let max = nums[0];
    let subSum = 0;

    nums.forEach((num) => {
        subSum = Math.max(subSum + num, num);

        if (max < subSum) {
            max = subSum;
        }
    });

    return max;
};

// 시간복잡도: O(n)
// 공간복잡도: O(1)
