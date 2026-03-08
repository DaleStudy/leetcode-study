/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
  let arrToSet = new Set(nums);
  
  const originalLength = nums.length;
  const filteredLength = arrToSet.size;

  if(originalLength === filteredLength){
    return false; // 겹치는 숫자가 없는 경우
  } else {
    return true; // 겹치는 숫자가 있는 경우
  }

};
