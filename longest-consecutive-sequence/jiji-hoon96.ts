/**
 * 연속된 숫자의 최대 길이를 구하는 문제
 * @param {number[]} nums
 * @return {number}
 *
 * 풀이
 *
 * nums 배열을 중복을 제거하고 오름차순으로 정렬한다.
 * 중복을 제거하고 정렬한 배열을 순회하면서 연속된 숫자의 길이를 구한다.
 */
function longestConsecutive(nums: number[]): number {
    if (nums.length === 0) return 0;
    const sortedNums = Array.from(new Set(nums)).sort((a, b) => a - b);

    if (sortedNums.length === 1) return 1;

    let currentCount = 1;
    let maxCount = 1;

    for(let i = 0; i < sortedNums.length - 1; i++) {
        const currentNum = sortedNums[i];
        const nextNum = sortedNums[i + 1];

        if(currentNum + 1 === nextNum) {
            currentCount++;
            maxCount = Math.max(maxCount, currentCount);
        } else {
            currentCount = 1;
        }
    }

    return maxCount;
}
