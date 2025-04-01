/**
 *
 * 접근 방법 :
 *  - set 자료구조에 nums 값 담아서 set의 크기와 배열의 길이를 비교하기
 *
 * 시간복잡도 : O(n)
 *  - nums 배열을 순회해서 set에 저장하니까 O(n)
 *
 * 공간복잡도 : O(n)
 *  - nums 배열의 길이만큼 set에 담으니까 O(n)
 */
function containsDuplicate(nums: number[]): boolean {
  return nums.length !== new Set([...nums]).size;
}
