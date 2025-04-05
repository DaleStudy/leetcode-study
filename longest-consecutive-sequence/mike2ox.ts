/**
 * Source: https://leetcode.com/problems/longest-consecutive-sequence/
 * 요점: 배열에서 가장 긴 연속된 정수 시퀀스의 길이를 반환
 * 풀이 시간: 48분
 * 풀이방법: 정렬 후 순회를 통해 연속된 값이 있는지 확인
 * 시간복잡도: O(nlogn) - 정렬이 지배적인 연산
 * 공간복잡도: O(1) - 추가 저장공간이 입력 크기에 비례하지 않음 (정렬은 in-place로 가정)
 */
function longestConsecutive(nums: number[]): number {
  // 엣지 케이스: 빈 배열이면 0 반환
  if (nums.length === 0) return 0;

  // 배열을 오름차순으로 정렬
  const sorted = nums.sort((a, b) => a - b);

  let maxLength = 1; // 가장 긴 연속 시퀀스 길이
  let currentLength = 1; // 현재 연속 시퀀스 길이
  let previousNum = sorted[0]; // 이전에 처리한 숫자

  // 정렬된 배열을 순회하며 연속 시퀀스 찾기
  for (let i = 1; i < sorted.length; i++) {
    const currentNum = sorted[i];

    // 중복된 값은 건너뜀
    if (previousNum === currentNum) {
      continue;
    }

    // 연속된 값인 경우 현재 시퀀스 길이 증가
    if (currentNum === previousNum + 1) {
      currentLength++;
    } else {
      // 연속이 끊긴 경우, 최대 길이 업데이트 후 현재 시퀀스 길이 초기화
      maxLength = Math.max(maxLength, currentLength);
      currentLength = 1;
    }

    previousNum = currentNum;
  }

  // 마지막 시퀀스의 길이와 최대 길이 비교하여 최종 결과 반환
  return Math.max(maxLength, currentLength);
}
