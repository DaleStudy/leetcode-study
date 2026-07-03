/**
 * @param {number[]} nums
 * @return {number}
 */
function longestConsecutive(nums) {
  let set_nums = new Set(nums);
  let max_seq = 0;

  if (set_nums.size === 0) return 0;

  for (let num of set_nums) {
    // num-1이 없는 경우 num이 시작 수
    if (!set_nums.has(num - 1)) {
      let curNum = num;
      let seq = 1; // 시작점이 된 순간 seq=1

      while (set_nums.has(curNum + 1)) {
        curNum += 1;
        seq += 1;
      }
      max_seq = Math.max(max_seq, seq);
    }
  }
  return max_seq;
}
