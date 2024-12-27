/**
 * 계단 오르기
 * 알고리즘 복잡도:
 * - 시간복잡도: O(n) - 입력값 크기에 비례하는 단일 반복문
 * - 공간복잡도: O(1) - 상수 개의 변수만 사용
 * @param n
 */
function climbStairs(n: number): number {
    // 1 - 2 - 3 - 5 - 8 ... 규칙 발생
    if(n <= 3) return n

    // 접근 (1) - 시간복잡도가 너무 큼
    // return climbStairs(n - 1) + climbStairs(n - 2) // 시간

    // 접근 (2)
    // 피보나치 수열과 비슷한 앞의 두 숫자를 더해서 배열 구조를 만듬
    let current = 1;  // 현재 방법
    let prev = 1;     // 이전 단계의 방법

    // n-1번 반복하여 계산
    for (let i = 1; i < n; i++) {
        [current, prev] = [current + prev, current];
    }

    return current;
}
