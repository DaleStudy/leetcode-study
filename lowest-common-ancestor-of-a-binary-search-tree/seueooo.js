/**
 * 풀이
 * 1. 중복 제거 후 정렬
 * 2. 연속된 수의 개수를 세어 배열에 저장
 * 3. 배열을 내림차순으로 정렬 후 첫 번째 요소 반환
 * 시간 복잡도 - O(n log n) : 중복 제거 O(n) + 정렬 O(n log n)
 * 공간 복잡도 - O(n) : 중복 제거 후 새로운 배열 생성
 */
var longestConsecutive = function (nums) {
  let arr = [];
  let newNums = [...new Set(nums)];
  newNums.sort((a, b) => a - b);
  let count = 1;
  for (let i = 0; i < newNums.length - 1; i++) {
    if (newNums[i] + 1 === newNums[i + 1]) {
      count++;
    } else {
      arr.push(count);
      count = 1;
    }
  }
  // 마지막 그룹
  arr.push(count);
  arr.sort((a, b) => b - a);
  return arr[0];
};
