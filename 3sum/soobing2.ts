/**
 * 문제 유형
 * - Array (정렬 + 투포인터)
 * 
 * 문제 설명
 * - 3개의 수를 더해서 0이 되는 경우를 찾아서 배열로 반환하기
 * 
 * 아이디어
 * 1) 정렬 후 투포인터 사용, 중복 제거
 
 */
function threeSum(nums: number[]): number[][] {
  const result: number[][] = [];

  // sorting
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    // 중복 제거
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    let left = i + 1;
    let right = nums.length - 1;
    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];
      if (sum === 0) {
        result.push([nums[i], nums[left], nums[right]]);
        left++;
        right--;

        // 중복 제거
        while (left < right && nums[left] === nums[left - 1]) left++;
        while (left < right && nums[right] === nums[right + 1]) right--;
      } else if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
  }
  return result;
}
