/**
 * 주어진 숫자 `n`의 2진수 표현에서 1의 개수를 계산.
 * 
 * @param {number} n - 1의 개수를 계산할 숫자 (양의 정수)
 * @returns {number} - 2진수에서 1의 개수
 * 
 * 시간 복잡도: O(k) 
 * - `k`는 숫자 `n`의 2진수 표현 길이 (log2(n))
 * - `toString(2)` 연산과 배열 순회를 포함.
 * 
 * 공간 복잡도: O(k)
 * - 2진수 문자열과 문자열 배열을 저장하는 데 사용되는 메모리 포함.
 */
function hammingWeight(n: number): number {
    // 1. 입력 숫자 `n`을 2진수 문자열로 변환
    // 2. 2진수 문자열을 개별 문자로 나누어 배열로 변환
    // 3. 배열에서 1의 개수를 누적하여 합산
    return n.toString(2).split('').reduce((a, b) => a + Number(b), 0);
};

