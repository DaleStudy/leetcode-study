// TC: O(n)
// SC: O(1)
function missingNumber(nums: number[]): number {
  // 0, 1, 2, 3 => n * (n + 1) / 2

  let sum = (nums.length * (nums.length + 1)) / 2;

  for (const num of nums) {
    sum -= num;
  }

  return sum;
}


// TC: O(n)
// SC: (1)
// function missingNumber(nums: number[]): number {
//   let xor = 0;

//   for (let i = 0; i <= nums.length; i++) {
//     xor ^= i;
//   }

//   for (const num of nums) {
//     xor ^= num;
//   }

//   return xor;
// }
