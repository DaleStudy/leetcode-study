// TC: O(n)
// SC: O(1)
function maxProduct(nums: number[]): number {
  let prevMax = nums[0];
  let prevMin = nums[0];
  let maxProd = nums[0];

  for (let i = 1; i < nums.length; i++) {
    const currentNum = nums[i];
    const tempMax = Math.max(
      currentNum,
      prevMax * currentNum,
      prevMin * currentNum
    );
    prevMin = Math.min(currentNum, prevMax * currentNum, prevMin * currentNum);
    prevMax = tempMax;
    maxProd = Math.max(maxProd, prevMax);
  }

  return maxProd;
}


// TC: O(n^2)
// SC: O(1)
// function maxProduct(nums: number[]): number {
//   let largestProd = -Infinity;
//   let subProd = 1;

//   for (let i = 0; i < nums.length; i++) {
//     subProd = 1;
//     for (let j = i; j < nums.length; j++) {
//       subProd *= nums[j];
//       largestProd = Math.max(largestProd, subProd);
//     }
//   }

//   return largestProd;
// }

