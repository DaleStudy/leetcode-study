/**
 *
 * 접근 방법 :
 *  - 중복 숫자 제거한 뒤, 숫자 순회하면서 연속 숫자의 시작 지점인지 체크
 *  - 더 작은 숫자가 없으면 현재 숫자가 연속 숫자의 시작 지점이기 때문에, 연속된 다음 큰 숫자가 존재하는지 체크
 *  - 있으면 count 증가시키고, 그 다음 숫자 있는지 반복해서 체크
 *  - 연속 숫자가 존재하지 않을 때까지 순회하기
 *  - count가 maxCount보다 큰 경우 maxCount값을 count 값으로 업데이트
 *
 * 시간복잡도 :
 *  - 숫자 배열 길이를 모두 순회하니까 O(n)
 *
 * 공간복잡도 :
 *  - Set을 사용해서 숫자 중복 제거하고 저장하니까 O(n)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  // 배열 비어있는 경우 처리
  if (nums.length === 0) return 0;

  const uniqueNums = new Set(nums);
  let maxCount = 1;

  for (const num of uniqueNums) {
    // 연속된 숫자의 시작 지점인지 체크(더 작은 숫자가 존재하지 않아야 함)
    if (!uniqueNums.has(num - 1)) {
      let next = num + 1;
      let count = 1;

      // 연속 숫자가 더 존재하는지 체크
      while (uniqueNums.has(next)) {
        next++;
        count++;
      }

      // 기존 maxCount보다 크면, count 값으로 업데이트하기
      if (maxCount < count) maxCount = count;
    }
  }

  return maxCount;
};
