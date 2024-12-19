/**
 * @param {number[]} nums
 * @return {number}
 */

var rob = function (nums) {
  // 집이 하나인 경우
  if (nums.length === 1) return nums[0]

  let prevMax = 0 // 두 집 전까지의 최대 금액
  let currMax = 0 // 이전 집까지의 최대 금액

  for (let num of nums) {
    let temp = currMax // 현재 최대 금액
    currMax = Math.max(currMax, prevMax + num) // 현재 집을 털거나 털지 않을 경우 중 큰 값
    prevMax = temp // 이전 집으로 이동
  }

  return currMax // 최대 금액 반환
}
