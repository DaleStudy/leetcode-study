/**
 * 시간 복잡도: nums의 크기만큼 순회하므로 O(n)
 * 공간 복잡도: 상수 크기 변수 두 개만 사용하므로 O(1)
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
  let prev = 0, cur = 0;
  for (let num of nums) {
      let tmp = cur;
      cur = Math.max(cur, prev + num);
      prev = tmp;
  }
  return cur;
};

