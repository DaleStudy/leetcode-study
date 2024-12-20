/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

/*
두 수 더하기
nums: 숫자 배열
target: 목표 숫자

target 숫자에 맞게 nums 배열중 2개를 더함.
  return은 더한 두 수의 index
  - for i in nums -> target - i 값이 배열내에 있는지 찾기
*/
var twoSum = function (nums, target) {
  let indexArray = []; // 답을 저장할 배열
  for (let i = 0; i < nums.length; i++) {
    let tNum = nums.lastIndexOf(target - nums[i]); // 배열내에 target - nums[i] 찾기
    if (i === tNum) { // 같은 수 사용 방지

    }
    else if (tNum > 0 && indexArray.lastIndexOf(i) === -1) { // 배열내에 원하는 값이 있다면
      indexArray.push(i);
      indexArray.push(tNum);
      break;
    }
  }
  return indexArray;
};
