/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    if (nums.length === 0) return 0;

    const numSet = new Set(nums);
    let maxLength = 0;

    for (let num of numSet) {
        // 연속 수열의 시작점인지 확인
        if (!numSet.has(num - 1)) {
            let currentNum = num;
            let currentLength = 1;

            // 연속된 숫자 있는 동안 증가
            while (numSet.has(currentNum + 1)) {
                currentNum += 1;
                currentLength += 1;
            }

            maxLength = Math.max(maxLength, currentLength);
        }
    }

    return maxLength;
};
