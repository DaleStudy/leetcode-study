/*
answer[i] = numbers[0], ... numbers[i-1], numbers[i+1], ... number[n-1]의 곱임을 활용하여
nums를 1부터 n-1까지 순회하며 i-1까지의 곱을 answer[i]에 채우고, 
반대로 n-2부터 0까지 순회하며 i+1까지의 곱을 answer[i]에 채운다

시간복잡도 : O(N) => 2N번 순회
공간복잡도 : O(N) => number[] 배열 사용
*/

function productExceptSelf(nums: number[]): number[] {
  const answer = new Array(nums.length).fill(1)

  let multiVal = 1
  for (let i = 1; i < nums.length; i++) {
    multiVal *= nums[i - 1]
    answer[i] *= multiVal
  }

  multiVal = 1
  for (let i = nums.length - 2; i >= 0; i--) {
    multiVal *= nums[i + 1]
    answer[i] *= multiVal
  }

  return answer
}
