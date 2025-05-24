/**
 * 두 선을 선택해 물을 담을 수 있는 최대 면적을 구하는 문제
 *
 * 가로 길이: 두 선 사이의 거리(인덱스 차이)
 * 세로 길이: 두 선 중 더 짧은 높이(물은 낮은 쪽으로 넘치기 때문)
 * 면적 = 가로 길이 × 세로 길이
 *
 * 양쪽 끝에서 시작하는 두 포인터를 사용
 * 투 포인터 방식이 효율적인 이유: 항상 더 작은 높이를 가진 쪽을 이동시키면 최대 면적을 놓치지 않기 때문
 * 더 큰 높이 쪽을 이동시키면 가로 길이는 줄어들고, 세로 길이는 같거나 더 작아져서 면적이 줄어들 수밖에 없음
 *
 * 시간 복잡도: O(n) - 배열을 한 번만 순회
 * 공간 복잡도: O(1) - 추가 공간 사용 없음
 */
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let left = 0;
  let right = height.length - 1;
  let maxWater = 0;

  while (left < right) {
    // 현재 두 선으로 만들 수 있는 물의 양 계산
    const width = right - left;
    const minHeight = Math.min(height[left], height[right]);
    const water = width * minHeight;

    // 최대값 업데이트
    maxWater = Math.max(maxWater, water);

    // 더 작은 높이를 가진 쪽의 포인터를 이동시킴
    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return maxWater;
};
