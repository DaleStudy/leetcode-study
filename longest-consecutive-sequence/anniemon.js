/**
 * 시간 복잡도:
 *   set의 요소 중 연속하는 시퀀스의 첫번째 숫자일 때만
 *   while 루프를 실행
 *   따라서 요소당 최대 1회 순회
 *   즉, 시간 복잡도는 O(n)
 * 공간 복잡도:
 *   set은 중복이 없을 경우 최대 O(n)를 차지함
 *   즉, 공간 복잡도는 O(n)
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  const set = new Set(nums);
  let res = 0;
  for (const n of set) {
      let seqLen = 0, target = n;
      const isSeqStart = !set.has(target - 1);
      if (isSeqStart) {
          while (set.has(target)) {
              target++;
              seqLen++;
          }
      }
      res = Math.max(seqLen, res);
  }
  return res;
};
