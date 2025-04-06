/**
 * [Problem]: [238] Product of Array Except Self
 * (https://leetcode.com/problems/product-of-array-except-self/description/)
 */

function productExceptSelf(nums: number[]): number[] {
  // 시간 복잡도 O(n^2)
  // 공간 복잡도 O(n)
  // 시간 초과로 실패
  function doubleLoopFunc(nums: number[]): number[] {
    return nums.map((_, i) => nums.reduce((acc, cur, j) => (i === j ? acc : acc * cur), 1));
  }

  // 시간 복잡도 O(n)
  // 공간 복잡도 O(n)
  function separateFunc(nums: number[]): number[] {
    const length = nums.length;
    const result: number[] = new Array(length).fill(1);
    let leftProduct = 1;
    let rightProduct = 1;

    for (let i = 0; i < length; i++) {
      result[i] = leftProduct;
      leftProduct *= nums[i];
    }

    for (let i = length - 1; i >= 0; i--) {
      result[i] *= rightProduct;
      rightProduct *= nums[i];
    }

    return result;
  }

  return separateFunc(nums);
}
