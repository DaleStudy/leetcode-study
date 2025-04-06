/**
 * 문제 파악: 배열에 중복된 요소가 있는지 확인하는 문제
 * 만약 한 값이 배열에서 적어도 두 번 이상 나타난다면 true를, 모든 요소가 고유하다면 false를 반환
 *
 * 접근 방식:
 * Set 객체를 사용하여 중복된 요소를 확인
 * Set은 중복된 값을 허용하지 않기 때문에, 배열을 Set으로 변환한 후 길이를 비교하여 중복 여부를 확인
 * 배열의 길이와 Set으로 변환한 후의 길이를 비교
 * - 길이가 다르면 중복된 요소가 존재하므로 true 반환
 * - 길이가 같으면 중복된 요소가 존재하지 않으므로 false 반환
 * 시간 복잡도: O(n) - 배열을 한 번 순회하면서 Set에 요소를 추가하기 때문
 * 공간 복잡도: O(n) - Set에 최대 n개의 요소를 저장해야 하기 때문
 */

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  const uniqueSet = new Set(nums);
  return uniqueSet.size < nums.length;
};

/**
 * 내장메서드인 sort()를 사용하여 배열을 정렬한 후, 인접한 요소를 비교하여 중복된 요소가 있는지 확인하는 방법도 있다. -> 시간 복잡도 O(n log n)
 *
 * 성능비교:
 * Set() 사용 : Runtime: ✨15ms, Memory: 68MB
 * sort() 사용: Runtime: 69ms, Memory: 65.6MB
 *
 * */
