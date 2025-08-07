/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  for(var i = 0; i < nums.length; i++){
    let getNum = target - nums[i];
    let foundIndex = nums.indexOf(getNum);

    // foundIndex가 존재하고(-1이 아니고), 자기 자신이 아닌 경우
    if(foundIndex !== -1 && foundIndex !== i) {
      return [i, foundIndex];
    }
  }
};
console.log(twoSum([2, 7, 11, 15], 9)); // [0, 1]
console.log(twoSum([3, 2, 4], 6));      // [1, 2]
console.log(twoSum([3, 3], 6));         // [0, 1]
