/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

/*
    정수 배열 nums와 목표값 target이 주어졌을 때,
    두 수를 더해 target이 되는 인덱스를 반환하는 함수

    요청형식 : twoSum(nums, target)
    입력형식 : nums는 정수 배열, target은 정수
    출력형식 : target을 만족하는 두 수의 인덱스를 [i, j] 형태로 반환

    요청예시 : twoSum([2,7,11,15], 9)
    출력예시 : [0, 1]
*/
var twoSum = function(nums, target) {

    const map = new Map();

    for (let i=0; i<nums.length; i++) {

        const diff = target - nums[i];

        if (map.has(diff)) {
            return [map.get(diff), i];
        }

        map.set(nums[i],i);

    }
};

console.log(twoSum([2,7,11,15], 9));
console.log(twoSum([3,2,4], 6));
console.log(twoSum([3,3], 6)); 
