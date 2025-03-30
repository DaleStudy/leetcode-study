const twoSum = (nums, target) => {
  // 배열을 한 번 순회
  for (let i = 0; i < nums.length; i += 1) {
    // target숫자에서 현재 숫자를 뺀 숫자가 존재하는지 확인한다.
    const targetIndex = nums.indexOf(target - nums[i]);
    // targetIndex가 존재하고(-1이 아님), 현재 숫자와 같은 인덱스 숫자가 아니라면 반환한다.
    if (targetIndex !== -1 && i !== targetIndex) {
      return [i, targetIndex];
    }
  }
};

// 시간 복잡도는 O(n^2)
// 공간 복잡도는 O(1)
