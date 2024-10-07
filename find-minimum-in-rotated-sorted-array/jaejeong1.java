class Solution {
  public int findMin(int[] nums) {
    // TC: O(log N)
    // SC: O(1)
    var left = 1; // N번 회전해 이미 오름차순 정렬일 경우 0으로 시작하면 루프가 안끝남. 1로 시작
    var right = nums.length-1;

    while (left <= right) { // left가 right보다 작거나 같을때까지
      var mid = (left + right) / 2;
      if (nums[mid - 1] > nums[mid]) { // mid - 1 요소가 mid 보다 값이 크면 변곡점을 찾은 것. 그대로 반환
        return nums[mid];
      }

      if (nums[mid] > nums[0]) { // 변곡점이 아니고, 0번째 인덱스보다 mid 요소가 값이 크면 정렬이 잘 되어 있는것. 오른쪽으로 탐색
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }

    return nums[0]; // N번 회전해 이미 오름차순 정렬일 경우 0번째 인덱스 요소 반환
  }
}
