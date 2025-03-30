/**
 * @param {number[]} nums
 * @return {boolean}
 */

/**
 * 문제설명: 2개 이상 반복되는 값이 있으면 true, 모두 반복되지 않으면 false.

제한사항
 1 <= nums.length <= 10^5
-109 <= nums[i] <= 109
 */

var containsDuplicate = function (nums) {
  const numberSet = new Set();
  //시간 복잡도 O(n)
  for (i of nums) {
    if (!numberSet.has(i)) {
      //공간복잡도 O(n)
      numberSet.add(i);
    } else {
      return true;
    }
  }
  return false;
};
