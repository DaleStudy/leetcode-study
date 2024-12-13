// 시간복잡도: O(n)

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  // Set을 사용해 중복 제거
  const numSet = new Set(nums);
  let longestStreak = 0;

  // 각 숫자를 기준으로 연속 시퀀스를 탐색
  for (let num of numSet) {
    // num이 시퀀스의 시작점인 경우만 탐색
    if (!numSet.has(num - 1)) {
      let currentNum = num;
      let currentStreak = 1;

      // 현재 시퀀스를 따라가며 길이 계산
      while (numSet.has(currentNum + 1)) {
        currentNum++;
        currentStreak++;
      }

      // 최대 길이를 업데이트
      longestStreak = Math.max(longestStreak, currentStreak);
    }
  }

  return longestStreak;
};