/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  // [-1,1,0,-3,3]
  if (!nums.includes(0)) {
    const allNumsProduct = nums.reduce((acc, cur) => acc * cur);
    return nums.map((num) => allNumsProduct / num);
  } else {
    let arr = [];
    for (let i = 0; i < nums.length; i++) {
      if (nums[i] !== 0) {
        arr[i] = 0;
      } else {
        console.log("여기는?");
        const newArr = [...nums];
        newArr.splice(i, 1);
        console.log("newArr ==>", newArr);
        if (newArr.includes(0)) {
          arr[i] = 0;
        } else {
          const product = newArr.reduce((arr, cur) => arr * cur);
          console.log("product ==>", product);
          arr[i] = product;
        }
      }
    }
    return arr;
  }
};
