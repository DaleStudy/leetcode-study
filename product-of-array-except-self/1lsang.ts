// 배열에서 인덱스의 숫자만 제외한 원소의 곱의 배열을 return 하는 문제

// 1. 전체의 곱을 구한 뒤, 해당 인덱스의 수를 나눈 배열을 만들면, 
//    n을 2번만 반복하면 되므로 2n 즉, O(n)으로 해결 가능

// 2. 하지만 수에 0이 섞여있다면?
//    0을 곱한 경우는 전부 0이므로 해당 케이스 고려 필요
//    0이 1개인 경우 0이 아닌 모든 수의 곱이 0인 인덱스에 들어가고, 나머지는 0
//    0이 2개 이상인 경우 전부 0

function productExceptSelf(nums: number[]): number[] {
  const zeroIndices:number[] = [];
  nums.forEach((num, index) => {
    if (num === 0) {
      zeroIndices.push(index);
    }
  })
  if (zeroIndices.length > 1) return Array.from({length: nums.length}).map(() => 0);
  const productOfAll = nums.reduce((prev, cur) => (cur === 0 ? prev : prev * cur), 1);
  if (zeroIndices.length === 1) return Array.from({length: nums.length}).map((_, index) => index === zeroIndices[0] ? productOfAll : 0);
  return nums.map((num) => productOfAll/num);
};
