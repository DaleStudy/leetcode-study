
// 풀이 1
// /**
//  * @param {number[]} nums
//  * @return {number[]}
//  */
// var productExceptSelf = function(nums) {
//     let hasZero = false;
//     const allProductNums = nums.reduce((acc, cur) => {
//         if (cur === 0) {
//             if (!hasZero) {
//                 hasZero = true;
//                 return acc;
//             }

//             return 0;
//         }
//         return acc * cur;
//     }, 1);

//     return nums.map(num => {
//         if (num === 0) {
//             return allProductNums;
//         }

//         return hasZero ? 0 : allProductNums / num;
//     });
// };

//풀이 2
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const result = Array(nums.length).fill(1);

    let beforeProductNum = 1;
    for (let i = 0; i < nums.length; i++) {
        result[i] *= beforeProductNum;
        beforeProductNum *= nums[i];
    }

    let afterProductNum = 1;
    for (let i = nums.length - 1; i >= 0; i--) {
        result[i] *= afterProductNum;
        afterProductNum *= nums[i];
    }

    return result;
};


//두 풀이 모두 시간 복잡도 O(n), 공간 복잡도는 O(n)
