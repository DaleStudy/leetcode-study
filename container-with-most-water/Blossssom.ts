/**
 * @param height - 정수 배열
 * @returns - 용기에 담을 수 있는 최대 물의 양
 * @description
 * - 양 끝에서 2포인터를 사용해 크기를 체크해 나아감
 * - 결국 거리가 짧아지기 때문에 양쪽 높이를 비교하며 높이가 낮은 포인터를 움직이며 계산
 * - 시간 복잡도 O(n)
 */

function maxArea(height: number[]): number {
  let left = 0;
  let right = height.length - 1;
  let water = 0;

  while (left < right) {
    const calcWater = (right - left) * Math.min(height[left], height[right]);
    if (water < calcWater) {
      water = calcWater;
    }

    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return water;
}

const height = [1, 3, 2, 5, 25, 24, 5];
const result = maxArea(height);


