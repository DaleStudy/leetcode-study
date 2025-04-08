/**
 * 시간복잡도: O(n)
 *  - 첫번째 for문 O(n)
 *  - 두번째 for문 O(n)
 *
 * 공간 복잡도: O(1)
 *  - 추가 배열 생성 X
 */
// const productExceptSelf = (nums) => {
//   let multiplyResult = 1;
//   let countZero = 0;

//   for (let i = 0; i < nums.length; i += 1) {
//     if (nums[i] === 0) {
//       countZero += 1;

//       if (countZero >= 2) {
//         multiplyResult = 0;
//         break;
//       }

//       continue;
//     }
//     multiplyResult *= nums[i];
//   }

//   for (let i = 0; i < nums.length; i += 1) {
//     if (countZero === 1) {
//       if (nums[i] === 0) {
//         nums[i] = multiplyResult;
//       } else {
//         nums[i] = 0;
//       }
//     } else if (countZero >= 2) {
//       nums[i] = 0;
//     } else {
//       nums[i] = multiplyResult / nums[i];
//     }
//   }

//   return nums;
// };

// 누적 합 이용
const productExceptSelf = (nums) => {
  const result = Array(nums.length).fill(1);

  let prefix = 1;

  for (let i = 0; i < nums.length; i += 1) {
    result[i] = prefix;
    prefix *= nums[i];
  }

  let postfix = 1;

  for (let i = nums.length - 1; i >= 0; i -= 1) {
    result[i] *= postfix;
    postfix *= nums[i];
  }

  return result;
};
