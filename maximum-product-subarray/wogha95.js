// TC: O(N)
// SC: O(1)

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
  let maximumProduct = Number.MIN_SAFE_INTEGER;
  let subProduct = 1;
  // 1. 좌에서 우로 누적곱을 저장하기 위해 순회
  for (let index = 0; index < nums.length; index++) {
    // 2. 0을 만나면 누적곱에 곱하지 않고 1로 초기화
    if (nums[index] === 0) {
      maximumProduct = Math.max(maximumProduct, 0);
      subProduct = 1;
      continue;
    }
    // 3. 매번 누적곱을 갱신
    subProduct *= nums[index];
    maximumProduct = Math.max(maximumProduct, subProduct);
  }

  subProduct = 1;
  // 4. 우에서 좌로 누적곱을 저장하기 위해 순회
  for (let index = nums.length - 1; index >= 0; index--) {
    // 5. 0을 만나면 누적곱에 곱하지 않고 1로 초기화
    if (nums[index] === 0) {
      maximumProduct = Math.max(maximumProduct, 0);
      subProduct = 1;
      continue;
    }
    // 6. 매번 누적곱을 갱신
    subProduct *= nums[index];
    maximumProduct = Math.max(maximumProduct, subProduct);
  }

  return maximumProduct;
};
