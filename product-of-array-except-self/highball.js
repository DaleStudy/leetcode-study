/* -------------------------------------------------------------------------- */
/*              time complexitiy: O(n),  space complexitiy: O(n)              */
/* -------------------------------------------------------------------------- */

// const productExceptSelf = function (nums) {
//   const result = [];
//   const n = nums.length;

//   if (n < 2) return result;

//   const left = [1];
//   const right = [1];

//   for (let i = 1; i < n; i++) {
//     left[i] = left[i - 1] * nums[i - 1];
//   }

//   for (let i = 1; i < n; i++) {
//     right[i] = right[i - 1] * nums[n - i];
//   }

//   for (let i = 0; i < n; i++) {
//     result[i] = left[i] * right[n - 1 - i];
//     if (result[i] === 0) result[i] = Math.abs(result[i]); //0이 -0으로 표시되는 이슈 핸들
//   }

//   return result;
// };

/* -------------------------------------------------------------------------- */
/*              time complexitiy: O(n),  space complexitiy: O(1)              */
/* -------------------------------------------------------------------------- */

const productExceptSelf = function (nums) {
  const result = [1];
  const n = nums.length;

  if (n < 2) return result;

  let prefix = 1;
  let postfix = 1;

  for (let i = 1; i < n; i++) {
    prefix *= nums[i - 1];
    result[i] = prefix;
    if (i === n - 1 && result[i] === 0) result[i] = Math.abs(result[i]); //0이 -0으로 표시되는 이슈 핸들
  }

  for (let i = n - 2; i >= 0; i--) {
    postfix *= nums[i + 1];
    result[i] *= postfix;
    if (result[i] === 0) result[i] = Math.abs(result[i]); //0이 -0으로 표시되는 이슈 핸들
  }

  return result;
};
