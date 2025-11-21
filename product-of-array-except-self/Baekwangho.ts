/**
[첫번째 시도]
O(n)의 시간 복잡도로, i 번째 수를 제외한 제곱 수 합을 구하는 문제
nums 를 좌우에서 순회하며, result += nums[i]^2 or nums[n-i]^2 를 이어 나가되,
두 배열을 더하는 시점에서 nums 의 배열 값을 뺴주면?

... 문제를 잘못 이해해서 합인 줄 알았다.. 곱이구나 나눗셈 없이 이를 어떻게 구한담

일단 nums 에 0이 두개 있으면 정답 배열의 모든 수는 0이다.
그 외에는 곱셈을 유지해야 하는데..

두 배열을 만들어서, 전체 수 곱 행렬을 만들어 보자 => 실패

수식으로 나타내보면?

f(n) = n번째 수 제외 전체 곱
f(0) = f(1) * ... * f(n)
f(1) = f(0) * f(2) * ... * f(n)
f(n-1) = f(0) * ... * f(n-2) * f(n)

모르겠다.. 오늘은 해설 보고 내일 기억해서 풀어보자
function productExceptSelf(nums: number[]): number[] {
  const forward = [nums[0]];
  const backward = [nums[nums.length - 1]];

  for (let i = 1; i < nums.length; i++) {
    forward.push(forward[i - 1] * nums[i]);
    backward.push(backward[i - 1] * nums[nums.length - 1 - i]);
  }

  const result = [];
  for (let i = 0; i < nums.length - 1; i++) {
    result.push(forward[i] * backward[i]);
  }

  return result;
}

 */
/**
[두번째 시도]
접근은 맞았다. 결국 제대로 수식을 작성해야 하는 듯
수식을 작성해보면, 
forward 는 [1, 2, 2*3, 2*3*4]
backward 는 [3*4*5, 4*5, 5, 1] 가 나와야 한다.

시간 복잡도: O(2n)
공간 복잡도: O(3n)
*/

function productExceptSelf(nums: number[]): number[] {
  const forward = [1]
  const backward = [1]
  for (let i=0; i<nums.length-1; i++) {
    forward.push(nums[i] * forward[i])
    backward.push(nums[nums.length-1-i] * backward[i])

  }

  const result = []
  for (let i=0; i<nums.length; i++){
    result.push(forward[i] * backward[nums.length-1-i])
  }

  return result
}
