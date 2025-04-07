/**
 * 주어진 배열의 숫자들로 만들 수 있는 가장 긴 연속 수열의 길이를 반환하는 함수
 * @param {number[]} nums
 * @return {number}
 */
const longestConsecutive = function(nums) {
    const sorted = Array.from(new Set(nums)).sort((a, b) => Number(a) - Number(b));

    let maxLength = 0;
    let currentSequenceLength = 0;

    for (let i = 0; i < sorted.length; i++) {
        if (i === 0) {
            maxLength = 1;
            currentSequenceLength = 1;
            continue;
        }

        if (sorted[i] === sorted[i - 1] + 1) {
            currentSequenceLength += 1;
        } else {
            currentSequenceLength = 1;
        }

        maxLength = Math.max(maxLength, currentSequenceLength);
    }

    return maxLength;
};

// 시간복잡도: O(n)
// 공간복잡도: O(n)
