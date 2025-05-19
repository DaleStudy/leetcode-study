function findMin(nums: number[]): number {
  let low = 0,
    high = nums.length - 1;

  while (low <= high) {
    let mid = Math.floor((low + high) / 2);
    if (nums[mid - 1] > nums[mid]) {
      return nums[mid]; // 회전이 일어난 곳
    }
    if (nums[0] < nums[mid]) {
      low = mid + 1; // 왼쪽은 이미 정렬되어 있어, 오른쪽으로 이동
    } else {
      high = mid - 1; // 왼쪽으로 이동
    }
  }
  return nums[0];
}
