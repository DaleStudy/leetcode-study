/***
 * 
 * @problem
 * - 배열에서 두 선을 선택하여 최대 물을 담을 수 있는 면적을 구하는 문제
 * 
 * @constraints
 * - 배열의 길이는 2 이상 10^5 이하입니다.
 * - 각 높이는 0 이상 10^4 이하의 정수입니다.
 * 
 * @example
 * - 입력: height = [1,8,6,2,5,4,8,3,7]
 * - 출력: 49
 *   (높이 8과 7을 선택하여 넓이 = min(8, 7) * (8 - 1) = 49)
 * 
 * @description
 * - 배열의 양 끝에서 시작하는 두 개의 포인터를 사용하여 문제를 해결합니다.
 * - 현재 포인터 위치에서의 넓이를 계산하고 최대값을 갱신합니다.
 * - 더 작은 높이를 가진 포인터를 이동하여 더 큰 넓이를 탐색합니다.
 * 
 * @complexity
 * - 시간 복잡도: O(n)
 *   (배열을 한 번만 순회하며 최대 넓이를 계산)
 * - 공간 복잡도: O(1)
 *   (추가 메모리 사용 없이 포인터만 사용)
 * 
 */
function maxArea(height: number[]): number {
    let left = 0, 
        right = height.length - 1, 
        maxArea = 0;

    while (left < right) {
        // 현재 넓이 계산 및 최대값 갱신
        maxArea = Math.max(maxArea, Math.min(height[left], height[right]) * (right - left));

        // 더 작은 높이의 포인터를 이동
        height[left] < height[right] ? left++ : right--;
    }

    return maxArea;
}
