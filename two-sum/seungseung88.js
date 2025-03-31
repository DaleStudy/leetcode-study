// 배열을 한 번 도니 시간 복잡도 O(n)
// 최악의 경우 nums의 크기 배열만큼 증가하므로 공간 복잡도는 O(n)

const twoSum = (nums, target) => {
  // {값: 인덱스} 형태로 저장
  const indicies = {};

  for (let i = 0; i < nums.length; i += 1) {
    // 타겟값에서 현재 가리키는 숫자를 뺀 값을 저장
    const complement = target - nums[i];

    // complement가 indicies안에 존재하면 해당 값을 반환
    if (complement in indicies) {
      const j = indicies[complement];
      return [j, i];
    }
    // 존재 하지 않으면 값과 인덱스 형태로 저장 ex> { 11: 0, 15: 1, 2: 2 }
    indicies[nums[i]] = i;
    console.log(indicies);
  }
};
