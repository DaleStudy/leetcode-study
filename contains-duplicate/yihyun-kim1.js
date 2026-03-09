/**
 * @param {number[]} nums
 * @return {boolean}
 */

// Set은 중복을 자동으로 제거하므로 Set의 크기가 원래 배열 길이보다 작으면 중복이 존재한다는 것
const containsDuplicate = (nums) => new Set(nums).size !== nums.length;
