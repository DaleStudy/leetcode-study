/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
    while (1 < nums.length) {

        const mid = Math.floor(nums.length / 2);

        const firstToHalf = [...nums].slice(0, mid);

        const midToEnd = [...nums].slice(mid, nums.length);

        const isInFront = Math.min(...firstToHalf) < Math.min(...midToEnd);

        nums = isInFront ? firstToHalf : midToEnd;
    }

    return nums[0];
};

// 시간복잡도 0(logn) -> 이진탐색을 통해 배열 nums를 반으로 쪼개가며 해답을 찾기때문에 
// 공간복잡도 O(n) -> 처음 while문이 돌 때, nums를 쪼갠 두 배열 총 길이의 합은 nums의 처음 길이와 같기때문에
