/**
 *
 * 문제 설명
 * 가장 많이 담을 수 있는 물의 용기 구하기
 * - height: 높이(n)를 담고 있는 배열 = y축 값
 * - index: x축 값
 *
 * 아이디어
 * 1. 브루트포스 방식  O(n^2)
 * - 모든 쌍을 비교하여 최대 물의 양 찾기
 *
 * 2. 투 포인터 방식 O(n)
 * - 왼쪽과 오른쪽 포인터를 이용하여 최대 물의 양 찾기
 * - 같은 높이의 두 라인이 있는 경우 한쪽만 움직여도 최적의 해를 찾는데는 문제 없음
 */
function maxArea(height: number[]): number {
  let left = 0;
  let right = height.length - 1;
  let result = 0;
  while (left < right) {
    const x = right - left;
    const y = Math.min(height[left], height[right]);
    result = Math.max(x * y, result);

    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return result;
}
