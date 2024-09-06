/*
* 조건
* 가장 큰 배열 곱을 찾아서 return
* 32-bit integer
* -10<=num[i]<=10

* 아이디어
* 이전 최대값, 최소값을 구해둔다
* 최대곱이 나올 수 있는 경우
* 1) 최소값 곱한것(-*-) 
* 2) 최대값 곱한것(+*+)
* 3) 자기자신인 경우(+)
* 배열을 돌면서 세 가지 중 최대최소값을 갱신해나간다
* 
*/
function maxProduct(nums: number[]): number {
  let max = nums[0];
  let min = nums[0];
  let result = nums[0];

  for (let i = 1; i < nums.length; i++) {
    const candidates = [nums[i] * max, nums[i], nums[i] * min];
    let currMax = Math.max(...candidates);
    let currMin = Math.min(...candidates);

    max = currMax;
    min = currMin;

    result = Math.max(currMax, result);
  }
  return result;
}

// TC: O(n)
// SC: O(1)
