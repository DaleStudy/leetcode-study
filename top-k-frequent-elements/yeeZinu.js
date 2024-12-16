/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 *
 * nums 배열 내 최빈도 숫자 k개 출력
 * 
 */
var topKFrequent = function (nums, k) {
  // 빈도 체크할 객체 
  let frequent = {};

  for (let i = 0; i < nums.length; i++) {
    // 숫자 중복될때마다 +1
    if (frequent[nums[i]] > 0) {
      frequent[nums[i]]++;
    }
    // 없으면 1로 초기화
    else {
      frequent[nums[i]] = 1;
    }
  }

  // 정렬을 위해 entries를 사용해 배열로 변환 
  const frequentEntries = Object.entries(frequent);
  frequentEntries.sort((a, b) => b[1] - a[1]);  // 내림차순 정렬

  // k갯수만큼 배열 자르기 및 배열 내부 값 number로 변경
  const topK = frequentEntries.slice(0, k).map((i) => Number(i[0]));
  return topK;
};
