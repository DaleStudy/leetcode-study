/**
풀이
- JS 집합 자료구조인 Set을 활용합니다. Set은 중복값이 들어올 경우 제거되어 고유한 값들만 갖는 특성이 있습니다.
- nums를 Set으로 바꾸고 두 데이터의 length(Set의 경우 size 접근자 사용)를 비교합니다.
  - 다를 경우 : Set에서 중복값이 제거된 경우이므로 true를 반환합니다.
  - 같을 경우 : 중복값이 없던 경우이므로 false를 반환합니다.

Big O
- Time Complexity: O(N) (N은 nums의 길이)
  new Set(nums)를 만드는 과정에서 배열의 모든 원소를 순회하며 Set에 삽입합니다. (삽입 평균 시간 O(1))
  numSet.size 및 nums.length는 각각 O(1)이므로 총 O(N)의 시간복잡도를 갖습니다.
- Space Complexity: O(N)
  Set에 최대 n개의 요소가 저장되므로 O(N)의 공간복잡도를 갖습니다.  
 */

function containsDuplicate(nums: number[]): boolean {
  const numSet = new Set(nums)
  return numSet.size !== nums.length
}
