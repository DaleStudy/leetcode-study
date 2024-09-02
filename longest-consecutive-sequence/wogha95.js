/**
 * TC: O(N)
 * SC: O(N)
 * nums의 숫자에 접근하는 횟수는 2번에서 N만큼, 4번에서 최대 N만큼 입니다.
 * 즉, 2N번 만큼 nums의 숫자에 접근합니다.
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  let maxCount = 0;
  const obj = {};

  // 1. 숫자의 존재 여부를 키로 접근하기 위해 저장
  for (const num of nums) {
    obj[num] = true;
  }

  // 2. 시작점들을 찾기 위해 순회
  for (const num of nums) {
    // 3. 연속적인 배열의 시작점인지 확인
    if (obj[num - 1]) {
      continue;
    }

    // 4. 연속적인 배열의 시작점부터 끝점까지 순회
    let count = 1;
    let next = num + 1;
    while (obj[next]) {
      count += 1;
      next += 1;
    }

    // 5. 가장 긴 배열의 길이 갱신
    maxCount = Math.max(maxCount, count);
  }

  return maxCount;
};
