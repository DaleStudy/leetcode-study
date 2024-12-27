/**
 * 주어진 배열에서 자신의 인덱스를 제외한 나머지 요소들의 곱을 계산하는 함수
 *
 * @param {number[]} nums - 정수 배열
 * @returns {number[]} - 각 인덱스의 요소를 제외한 나머지 요소들의 곱을 구한 배열
 *
 * 1. 결과 배열 `result`를 1로 초기화.
 * 2. 왼쪽에서 오른쪽으로 순회하며 `left` 값을 이용해 기준 idx 이전의 값을 계산하여 `result`에 저장.
 * 3. 오른쪽에서 왼쪽으로 순회하며 `right` 값을 이용해 접미 기준 idx 이후의 값들을 계산 히야 `result`에 곱함. 
 * 4. 결과 배열 `result`를 반환.
 *
 * 시간 복잡도:
 * - 왼쪽에서 오른쪽 순회: O(n)
 * - 오른쪽에서 왼쪽 순회: O(n)
 * - 전체 시간 복잡도: O(n)
 *
 * 공간 복잡도:
 * - 추가 배열 없이 상수 공간 사용 (result는 문제의 요구 조건에 포함되지 않음).
 * - 전체 공간 복잡도: O(1)
 */
function productExceptSelf(nums: number[]): number[] {
    const numLength = nums.length;
    const result = new Array(numLength).fill(1);

    let left = 1;
    for (let i = 0; i < numLength; i++) {
        result[i] *= left;
        left *= nums[i];
    }

    let right = 1;
    for (let i = numLength; i >= 0; i--) {
        result[i] *= right;
        right *= nums[i];
    }

    return result;
}
