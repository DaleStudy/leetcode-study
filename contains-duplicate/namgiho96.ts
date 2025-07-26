/**
 * @param {number[]} nums
 * @return {boolean}
 * @Description
 * 1. Set을 사용하여 중복된 값을 확인한다.
 * 2. Set의 크기가 nums의 길이와 다르면 중복된 값이 있다는 의미이므로 true를 반환한다.
 * 3. Set의 크기가 nums의 길이와 같으면 중복된 값이 없다는 의미이므로 false를 반환한다.
 */

function containsDuplicate(nums: number[]): boolean {
  return new Set(nums).size !== nums.length;
}
