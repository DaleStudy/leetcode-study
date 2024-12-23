function threeSum(nums: number[]): number[][] {
  if (nums.length < 3) return [];
  const result: number[][] = [];
  const checked = new Set<string>();
  const numMap = new Map<number, number>();

  // 중복 결과 방지
  nums.sort((a, b) => a - b);
  // Map에 모든 값과 인덱스 저장
  nums.forEach((num, index) => numMap.set(num, index));

  for (let i = 0; i < nums.length - 2; i++) {
    if (nums[i] > 0) break; // 양수면 존재 X
    // 중복된 첫 번째 수 건너뛰기
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    for (let j = i + 1; j < nums.length - 1; j++) {
      // 중복된 두 번째 수 건너뛰기
      if (j > i + 1 && nums[j] === nums[j - 1]) continue;
      // 세 번째 수 계산
      const target = -(nums[i] + nums[j]);

      // Map을 사용하여 세 번째 수 검색
      if (numMap.has(target)) {
        const k = numMap.get(target)!;
        if (k > j) {
          // k가 j보다 커야 중복 방지
          const triplet = [nums[i], nums[j], nums[k]];
          const key = triplet.join(",");

          // Set을 사용하여 중복 결과 방지
          if (!checked.has(key)) {
            checked.add(key);
            result.push(triplet);
          }
        }
      }
    }
  }

  return result;
}
