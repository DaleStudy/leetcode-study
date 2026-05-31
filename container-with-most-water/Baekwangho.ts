/**
f((a,ax), (b,bx)) => min(ax, bx) * (b - a) (단, b > a)
라고 하자
(1,1) (2,8) => 1
(1,1) (3,6) => 2
(2,8) (3,6) => 6
(1,1) (4,2) => 3
(2,8) (4,2) => 4
(3,6) (4,2) => 2
...
(2,8) (5,5) => 15

근데 생각해보니, 순회하면서 가장 큰 왼쪽 봉을 구하고, 한칸씩 움직이며 그 봉으로부터의 너비를 계산하면 되는 것 같음.
그러다가 왼쪽 봉보다 더 큰 봉이 있다면 거기서부터 시작하되, 최댓값은 그대로 두기

를 생각했다가 보니, 투 포인터를 사용해서 가장 큰 수를 구하는 방법이 있을 것 같음.
힌트를 보니, 낮은 바를 항상 움직이라고 함.

시간 복잡도: o(n) / 공간 복잡도: o(1)
*/
function maxArea(height: number[]): number {
  let left = 0;
  let right = height.length - 1;
  let max = 0;

  while (left < right) {
    const ltemp = height[left];
    const rtemp = height[right];

    if (ltemp < rtemp) {
      left++;
    } else {
      right--;
    }

    const result = (right - left + 1) * Math.min(ltemp, rtemp);
    if (result > max) {
      max = result;
    }
  }

  return max;
}
