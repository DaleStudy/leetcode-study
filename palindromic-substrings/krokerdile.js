/**
 * @param {string} s
 * @return {number}
 * 
 * 시간복잡도: O(n^2)
 *    - 각 문자(i)를 중심으로 확장 → 최대 n번
 *    - 각 중심에서 양쪽으로 확장하면서 비교 → 최대 n번
 *    → O(n) * O(n) = O(n^2)
 *
 *  공간복잡도: O(1)
 *    - 추가 공간 없이 count 변수와 index만 사용
 *    - 문자열을 복사하거나 메모이제이션 하지 않음
 */
var countSubstrings = function(s) {
    let count = 0;

    // 전체 문자열을 순회하면서 각 위치를 팰린드롬 중심으로 잡음
    for (let i = 0; i < s.length; i++) {
        // 홀수 길이 팰린드롬: ex. "aba"
        helper(i, i);

        // 짝수 길이 팰린드롬: ex. "abba"
        helper(i, i + 1);
    }

    // 팰린드롬이 유지되는 동안 count 증가시키는 함수
    function helper(left, right) {
        // 조건이 맞을 때마다 좌우로 확장
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            count++; // 유효한 팰린드롬 하나 발견
            left--;
            right++;
        }
    }

    return count;
};