function maxSubArray(nums: number[]): number {
  // 배열이 비어 있는 경우 체크 (제약조건에 의해 발생하지 않지만, 견고한 코드를 위해)
  if (nums.length === 0) return 0;
  
  // 현재 부분 배열의 합과 전체 최대 부분 배열 합 초기화
  let currentSum = nums[0];
  let maxSum = nums[0];
  
  // 두 번째 요소부터 순회
  for (let i = 1; i < nums.length; i++) {
      // 현재 위치에서의 최대 부분 배열 합 계산
      // "이전까지의 합 + 현재 요소" vs "현재 요소부터 새로 시작"
      currentSum = Math.max(nums[i], currentSum + nums[i]);
      
      // 전체 최대값 업데이트
      maxSum = Math.max(maxSum, currentSum);
  }
  
  return maxSum;
}
