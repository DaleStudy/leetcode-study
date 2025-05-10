/**
 * 주어진 배열에서 (두 원소 중 작은 값) * (두 원소의 인덱스 차이)의 최댓값을 반환하는 함수
 * @param {number[]} height
 * @return {number}
 */
const maxArea = function(height) {
    let left = 0;
    let right = height.length - 1;
    let max = 0;

    while (left < right) {
        const w = right - left;
        const h = Math.min(height[left], height[right]);

        max = Math.max(max, w * h);

        if (height[left] <= height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return max;
};

// 시간복잡도: O(n)
// 공간복잡도: O(1)
