/**
 * TC: O(N)
 * SC: O(N)
 * nums의 숫자에 접근하는 횟수는 2번에서 N만큼, 4번에서 최대 N만큼 입니다.
 * 즉, 2N번 만큼 nums의 숫자에 접근합니다.
 * N^2이 아닌 이유: N^2이 아닌 2N으로 생각한 이유는 2번에서 N번의 순회를 하지만 각 순회가 서로에게 영향을 미치기 때문에 최대 순회는 2N으로 계산했습니다. (1번의 N 순회 제외)
 * @see https://github.com/DaleStudy/leetcode-study/pull/408#discussion_r1747071917
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
