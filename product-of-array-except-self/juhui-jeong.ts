/*
시간 복잡도: O(n)
공간 복잡도: O(1)
*/
function productExceptSelf(nums: number[]): number[] {
  const n = nums.length;
  const answer = new Array<number>(n);

  // 왼쪽 곱 채우기
  let leftProduct = 1;
  for (let i = 0; i < n; i++) {
    answer[i] = leftProduct;
    leftProduct *= nums[i];
  }

  // 오른쪽 곱 채우기
  let rightProduct = 1;
  for (let i = n - 1; i >= 0; i--) {
    answer[i] *= rightProduct;
    rightProduct *= nums[i];
  }
  return answer;
}

/*
// Time Limit Exceeded
function productExceptSelf(nums: number[]): number[] {
  let answer = [];
  for (let i = 0; i < nums.length; i++) {
    const mulOfNums = nums.reduce((accumulator, currentValue, currentIndex) => {
      if (currentIndex !== i) {
        return accumulator * currentValue;
      }
      return accumulator;
    }, 1);
    answer.push(mulOfNums);
  }
  return answer;
}
*/
