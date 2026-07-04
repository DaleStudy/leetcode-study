function productExceptSelf(nums) {
  const result = [];
  let product = 1;

  for (let i = 0; i < nums.length; i++) {
    result[i] = product;
    product *= nums[i];
  }

  product = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    result[i] *= product;
    product *= nums[i];
  }
  return result;
}

console.log(productExceptSelf([1, 2, 3, 4]));
