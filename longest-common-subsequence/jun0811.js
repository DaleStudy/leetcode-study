/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  const set = new Set();

  // set 생성 : O(n)
  for (const num of nums) {
    set.add(num);
  }

  let res = 0;

  // set 순회 : O(n)
  for (const num of set) {
    if (set.has(num - 1)) continue;
    let tmp = 1;
    let cur = num;
    // While 루프 전체: O(n)
    while (true) {
      const v = (cur += 1);
      if (set.has(v)) tmp += 1;
      else break;
    }
    if (tmp > res) res = tmp;
  }
  return res;
};
