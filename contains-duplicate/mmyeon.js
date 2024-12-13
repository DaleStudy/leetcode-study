/**
 * @param {number[]} nums
 * @return {boolean}
 */

/**
 *
 * 접근 방법
 *  - Set 객체 사용해서 숫자 중복 제거하기
 *  - 원본 배열과 길이 비교하기
 *
 * 시간복잡도 :
 *  - 배열 순회해서 요소 Set에 삽입 : O(n)
 *  - Set의 사이즈 크기 비교 : O(1)
 *
 * 공간복잡도 :
 *  - Set에 유니크한 숫자 저장 : O(n)
 */

var containsDuplicate = function (nums) {
  return new Set(nums).size !== nums.length;
};
