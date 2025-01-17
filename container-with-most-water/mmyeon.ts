/**
 *@link https://leetcode.com/problems/container-with-most-water/description/
 *
 * 접근 방법 :
 *  - 가장 많은 물의 양을 구하기 위해서 투 포인터 사용
 *  - 한 높이가 낮으면 다른 높이가 아무리 높아도 의미가 없어서, 작은 높이를 가진 포인터 이동하며 계산
 *  - 양 끝에서 포인터 이동할 때마다 최대값 갱신
 *
 * 시간복잡도 : O(n)
 *  - 두 포인터가 배열 양 끝에서 1번씩 이동하므로
 *
 * 공간복잡도 : O(1)
 *  - 포인터(left,right)와 최대값 변수만 사용
 */
function maxArea(height: number[]): number {
  let left = 0,
    right = height.length - 1,
    maxWater = 0;

  while (left < right) {
    const width = right - left;
    const minHeight = Math.min(height[left], height[right]);
    maxWater = Math.max(maxWater, width * minHeight);

    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return maxWater;
}
