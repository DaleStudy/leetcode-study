/**
 * @param {number[]} height
 * @return {number}
 */
/*
주어진 정수 배열 height는 여러 개의 세로 막대기 높이를 나타낸다.
각 막대기는 x축 위의 서로 다른 위치에 수직으로 세워져 있다.

i번째 막대기의 좌표는 (i, 0)에서 (i, height[i])이다.

이 막대기들 중에서 서로 다른 두 개의 막대기를 선택하면,
두 막대기와 x축이 만나 하나의 물을 담을 수 있는 용기(container)를 만들 수 있다.

문제 목표:
  - 두 막대기를 선택했을 때
  - 그 사이에 담을 수 있는 물의 양(면적)이 최대가 되도록 한다.
  - 그 최대 물의 양을 반환한다.

중요한 조건:
  1) 용기는 기울일 수 없다. (막대기는 항상 수직)
  2) 물의 높이는 선택한 두 막대기 중 더 낮은 높이로 결정된다.
  3) 물의 너비는 두 막대기 사이의 거리(인덱스 차이)이다.

즉,
  물의 양 = (두 막대기 사이 거리) × (두 막대기 중 더 낮은 높이)

입력 형식:
  - height: 정수 배열
  - n == height.length
  - 2 <= n <= 100,000
  - 0 <= height[i] <= 10,000

출력 형식:
  - 담을 수 있는 최대 물의 양 (정수)

예시:

  Example 1
    입력: height = [1,8,6,2,5,4,8,3,7]
    출력: 49
    설명:
      - 여러 막대기 쌍 중
      - 특정 두 막대기를 선택했을 때
      - 거리와 높이의 곱이 가장 커짐
      - 그 최대값이 49

  Example 2
    입력: height = [1,1]
    출력: 1
    설명:
      - 두 막대기 사이 거리 = 1
      - 더 낮은 높이 = 1
      - 물의 양 = 1 × 1 = 1
*/

var maxArea = function(height) {

    let leftIndex = 0;
    let rightIndex = height.length - 1;
    let maxValue = 0;

    while (leftIndex < rightIndex) {
        const width = rightIndex - leftIndex;
        let heightValue = 0;
        if (height[leftIndex] < height[rightIndex]){
            heightValue = height[leftIndex];
        }else {
            heightValue = height[rightIndex];
        }
        const area = width * heightValue;

        if (area > maxValue) {
            maxValue = area;
        }

        if (height[leftIndex] < height[rightIndex]) {
            leftIndex++;
        } else {
            rightIndex--;
        }
    }

    return maxValue;

};

console.log(maxArea([1,8,6,2,5,4,8,3,7]))
console.log(maxArea([1,1]))

