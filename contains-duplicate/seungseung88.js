// 시간 복잡도: O(n) => 배열을 한 번만 순회하므로
// 공간 복잡도: O(n) => 최악의 경우 모든 요소를 객체에 저장하므로
const containsDuplicate = (nums) => {
  const indices = {};

  // 배열을 한 번 순회
  for (let i = 0; i < nums.length; i += 1) {
    const num = nums[i];

    // 아직 등장하지 않은 숫자라면 객체에 기록
    if (!indices[num]) {
      indices[num] = 1;
    } else {
      // 이미 등장한 숫자라면 중복이므로 true 반환
      return true;
    }
  }

  // 중복이 없으면 false 반환
  return false;
};
