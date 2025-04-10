/*
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(n)
 */

/**
 * @param {number[]} nums
 * @return {number[]}
 */

var productExceptSelf = function(nums) {
  const lefts = nums.reduce((products, num, i) => {
      products.push(i === 0 ? 1 : products[i - 1] * nums[i - 1]);
      return products;
    }, []
  );

  return nums.reduceRight((result, num, i) => {
      const rights = i === nums.length - 1 ? 1 : result.rightProduct * nums[i + 1];
      result.products[i] *= rights;
      result.rightProduct = rights;
      return result;
    }, { products: lefts, rights: 1 }
  ).products;
};
