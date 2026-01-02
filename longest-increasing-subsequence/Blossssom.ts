/**
 * @param nums - 정수 배열
 * @returns - 엄격하게 증가하는 요소의 길이 반환
 */
function lengthOfLIS(nums: number[]): number {
  const arr: number[] = Array.from({ length: nums.length }, () => 1);
  let maxLen = 1;
  for (let i = 1; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[i] > nums[j]) {
        arr[i] = Math.max(arr[i], arr[j] + 1);
      }
    }
    maxLen = Math.max(maxLen, arr[i]);
  }

  return maxLen;
}

const nums = [0, 1, 0, 3, 2, 3];
lengthOfLIS(nums);


