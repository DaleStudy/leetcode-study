/**
 * @param {number[]} nums
 * @return {boolean}
 */

/*
    nums 배열이 주어졌을 때,
    중복된 값이 존재하면 true,
    중복된 값이 없으면 false를 반환하는 함수

    요청형식 : containsDuplicate(nums)
    입력형식 : nums는 정수 배열로 길이는 1 이상 10^5 이하, 각 원소는 -10^9 이상 10^9 이하

    요청예시 : containsDuplicate([1,2,3,1])
    출력예시 : true
*/
var containsDuplicate = function(nums) {
    
    const set = new Set(nums);

    if(nums.length != set.size){
        return true;
    }else {
        return false;
    }
};

// 테스트 실행
console.log("Example 1:", containsDuplicate([1, 2, 3, 1])); // true
console.log("Example 2:", containsDuplicate([1, 2, 3, 4])); // false
console.log("Example 3:", containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])); // true