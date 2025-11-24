/**
 * 복잡도 분석:
 * - 시간: O(n) - 배열을 두 번 순회 (왼쪽→오른쪽, 오른쪽→왼쪽)
 * - 공간: O(1) - answer 배열은 출력이므로 제외, rightProduct 변수만 사용
 */

/**
 * @param {number[]} nums
 * @return {number[]}
 */
const productExceptSelf = (nums) => {
  const n = nums.length;
  const answer = new Array(n);

  /**
   * 아이디어:
   * answer[i] = (i 왼쪽 모든 요소의 곱) × (i 오른쪽 모든 요소의 곱)
   *
   * 예시: [1, 2, 3, 4]
   * - 왼쪽 곱: [1, 1, 2, 6]
   * - 오른쪽 곱: [24, 12, 4, 1]
   * - 결과: [24, 12, 8, 6]
   */

  // 1단계: 왼쪽에서 오른쪽으로 순회하며 왼쪽 곱 저장
  answer[0] = 1; // 첫 번째는 왼쪽에 아무것도 없으므로 1
  for (let i = 1; i < n; i++) {
    answer[i] = answer[i - 1] * nums[i - 1]; // 이전까지의 곱 × 이전 요소
  }

  // 2단계: 오른쪽에서 왼쪽으로 순회하며 오른쪽 곱을 곱해줌
  let rightProduct = 1; // 오른쪽 곱을 누적할 변수
  for (let i = n - 1; i >= 0; i--) {
    answer[i] *= rightProduct; // 왼쪽 곱 × 오른쪽 곱
    rightProduct *= nums[i]; // 다음 순회를 위해 현재 요소 곱함
  }

  return answer;
};
