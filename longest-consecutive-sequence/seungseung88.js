/**
 * 시간복잡도: O(n)
 *    - set.has() => O(1)
 *    - while() => 최악의 경우 O(n)
 * 공간복잡도: new Set() => O(n)
 */
const longestConsecutive = (nums) => {
  // 빈 배열일 때 0 리턴
  if (nums.length === 0) return 0;

  // 중복 제거
  const set = new Set(nums);

  // 연속되는 숫자의 길이를 넣을 변수 설정
  let longest = 0;

  set.forEach((v) => {
    // 일단 연속되는 배열에서는 가장 최솟값을 찾음
    if (!set.has(v - 1)) {
      let cnt = 1;

      // 연속되는 배열에서 가장 긴 배열을 저장
      while (set.has(v + cnt)) {
        cnt += 1;
        longest = longest < cnt ? cnt : longest;
      }
    }
  });

  return longest;
};
