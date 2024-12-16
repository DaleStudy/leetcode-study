/**
 * 접근 방법 :
 *  - 숫자 바열을 전체 순회하면서 빈도수를 객체에 저장
 *  - 객체 값을 내림차순으로 정렬한 뒤, 원하는 항목만큼 자르고 숫자로 변환한 뒤 리턴하기
 *
 * 시간복잡도 : O(nlogn)
 *  - 숫자 배열 길이 = n , 가져올 항목 개수 = k
 *  - 객체에 숫자와 빈도수 저장하기 위해서 모든 숫자 순회  : O(n)
 *  - 객체 키값을 내림차순으로 정렬 : O(nlogn)
 *  - slice, map : O(k)
 *
 * 공간복잡도 :
 *  - 숫자 배열의 길이만큼 객체에 저장하니까 O(n)
 */

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

var topKFrequent = function (nums, k) {
  const obj = {};

  for (const num of nums) {
    obj[num] = (obj[num] ?? 0) + 1;
  }

  return Object.entries(obj)
    .sort((a, b) => b[1] - a[1])
    .slice(0, k)
    .map((item) => Number(item[0]));
};
