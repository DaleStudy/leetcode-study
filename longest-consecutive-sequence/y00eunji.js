/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const numSet = new Set(nums);
    let longestStreak = 0;

    for (const num of numSet) {
        // 현재 숫자가 연속 시퀀스의 시작점인지 확인
        // 즉, num-1이 set에 없어야 함
        if (!numSet.has(num - 1)) {
            let currentNum = num;
            let currentStreak = 1;

            // 현재 숫자의 연속된 다음 숫자들을 찾음
            while (numSet.has(currentNum + 1)) {
                currentNum += 1;
                currentStreak += 1;
            }

            longestStreak = Math.max(longestStreak, currentStreak);
        }
    }

    return longestStreak;
};
