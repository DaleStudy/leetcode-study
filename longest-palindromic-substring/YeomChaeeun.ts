/**
 * 중심 확장법을 이용하여 가장 긴 팰린드롬 찾기
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n2)
 * - 공간 복잡도: O(1)
 * @param s
 */
function longestPalindrome(s: string): string {
    let maxLength = 0;
    let longestPal = '';

    for (let x = 0; x < s.length; x++) {
        // 1. 홀수 길이 팰린드롬 - 한 문자를 중심으로 함
        let left = x
        let right = x

        while (left >= 0 && right < s.length && s[left] === s[right]) {
            // 현재 발견한 팰린드롬이 이전에 발견한 것보다 길면 갱신
            if (right - left + 1 > maxLength) {
                maxLength = right - left + 1;
                longestPal = s.substring(left, right + 1);
            }

            left--
            right++
        }

        // 2. 짝수 길이 팰린드롬 - 두 문자 사이를 중심으로 함
        left = x
        right = x + 1

        while (left >= 0 && right < s.length && s[left] === s[right]) {
            // 현재 발견한 팰린드롬이 이전에 발견한 것보다 길면 갱신
            if (right - left + 1 > maxLength) {
                maxLength = right - left + 1;
                longestPal = s.substring(left, right + 1);
            }

            left--
            right++
        }
    }

    return longestPal
}
