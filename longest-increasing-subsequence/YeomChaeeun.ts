/**
 * 주어진 배열에서 가장 긴 부분 수열의 길이 구하기
 * 달고알레 풀이를 참고하여 동적 프로그래밍 적용했습니다
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n2)
 * - 공간 복잡도: O(n)
 * @param nums
 */
function lengthOfLIS(nums: number[]): number {
    // dp 배열을 1로 초기화 - 각 숫자 단독의 기본 길이는 1임
    const dp: number[] = new Array(nums.length).fill(1)
    let maxLength = 1

    for (let i = 1; i < nums.length; i++) {
        // 현재 위치(i) 이전의 모든 원소들을 확인
        for (let j = 0; j < i; j++) {
            // 현재 숫자가 이전 숫자보다 큰 경우 - 부분 수열이 가능하다는 것
            if (nums[i] > nums[j]) {
                dp[i] = Math.max(dp[i], dp[j] + 1)
            }
        }
        maxLength = Math.max(maxLength, dp[i])
    }

    return maxLength
}
