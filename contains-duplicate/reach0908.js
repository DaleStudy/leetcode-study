/**
 * @description
 * time complexity: O(n)
 * space complexity: O(n)
 * 풀이 방법:
 *  - 주어진 배열을 순회하며 해쉬테이블을 구성하고 해쉬 테이블에 이미 값이 있는 경우 early return 을 통해 중복됨을 반환
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicate = function (nums) {
  const hashTable = new Set();
  for (let i = 0; i < nums.length; i++) {
    if (hashTable.has(nums[i])) {
      return true;
    }
    hashTable.set(nums[i], i);
  }
  return false;
};
