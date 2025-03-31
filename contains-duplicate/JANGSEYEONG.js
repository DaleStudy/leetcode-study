// 시간복잡도: O(n) - Set 생성 시 모든 요소를 한 번씩 처리하기 때문
// - new Set(nums)는 배열의 모든 요소를 순회하며 Set에 추가: O(n)
// - 길이 비교 자체는 O(1)이므로 전체 시간복잡도는 O(n)
var containsDuplicate = function (nums) {
  // Set으로 만들었을 때, 기존 배열과 사이즈가 다르면 중복이 제거된거임
  const numsSet = new Set(nums);
  return nums.length !== numsSet.size;
};
