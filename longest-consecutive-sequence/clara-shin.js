/**
 * 분류되지 않은 정수 배열이 주어질 때, 가장 긴 연속 요소 시퀀스의 길이를 리턴하는 문제
 * 조건: 시간복잡도 O(n)
 * 
 * 접근 방식:
 * (1) 빈 배열이면 0 반환하고 빠른 탈출
 * (2) Set을 사용하여 중복 제거 및 빠른 조회
 * (3) Set을 순회하면서 연속 시퀀스의 시작점인지 확인(시작점만 처리해줌)
 * (4) 시작점이면 연속되는 숫자를 찾아 길이 계산하고
 * (5) 최대 길이 갱신해준 후 리턴
 * 
 * /

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  if (nums.length === 0) return 0;

  const numSet = new Set(nums);
  let maxLength = 0;

  for (const num of numSet) {
    if (!numSet.has(num - 1)) {
      let currentNum = num;
      let currentLength = 1;

      while (numSet.has(currentNum + 1)) {
        currentNum++;
        currentLength++;
      }

      maxLength = Math.max(maxLength, currentLength);
    }
  }

  return maxLength;
};
