// 시간복잡도 O(n2)
// 공간복잡도 O(k) (k는 결과 개수)
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort((a, b) => a - b);

    let result = []

    for (let i = 0 ; i <= nums.length - 2; i++) {
        if (i > 0 && nums[i] === nums[i-1]) continue

        const curNum = nums[i]
        let leftIdx = i+1;
        let rightIdx = nums.length - 1;

        while (leftIdx < rightIdx) {
            const leftNum = nums[leftIdx]
            const rightNum = nums[rightIdx]
            const threeSum = curNum + leftNum + rightNum
            if (threeSum === 0) {
                result.push([curNum, leftNum, rightNum])
                while (leftIdx < rightIdx && nums[leftIdx] === nums[leftIdx+1]) leftIdx++
                while (leftIdx < rightIdx && nums[rightIdx] === nums[rightIdx-1]) rightIdx--
                leftIdx++
                rightIdx--
            } else if (threeSum < 0) {
                leftIdx = leftIdx + 1
            } else if (threeSum > 0) {
                rightIdx = rightIdx - 1
            }
        }

    }

    return result
};
