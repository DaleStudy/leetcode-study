/**
 * @param {number[]} nums
 * @return {number}
 */

var longestConsecutive = function (nums) {
  // Set으로 배열에서 중복된 요소 제거
  const numSet = new Set(nums)

  // 최장 길이
  let longest = 0

  // 배열을 돌며 첫 시작이 되는 숫자를 찾음
  for (const num of numSet) {
    // 연속된 숫자의 시작은 num - 1이 Set에 존재하지 않는 숫자여야 함
    if (!numSet.has(num - 1)) {
      let currentNum = num
      let currentStreak = 1
      
      while (numSet.has(currentNum + 1)) {
        currentNum += 1 // 다음 숫자로 이동
        currentStreak += 1 // 연속된 길이 증가
      }

      longest = Math.max(longest, currentStreak)
    }
  }

  return longest
}
