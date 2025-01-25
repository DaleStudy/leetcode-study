/**
 * 중복된 문자가 없는 가장 긴 부분 문자열 구하기
 * 달레 알고리즘 해설을 참고하여 작성했습니다
 * 슬라이딩 윈도우 방식 적용
 * 알고리즘 복잡도
 * - 시간 복잡도: O(n)
 * - 공간 복잡도: O(n)
 * @param s
 */
function lengthOfLongestSubstring(s: string): number {
    const set = new Set<string>();
    let start = 0;
    let end = 0;
    let maxLength = 0;

    while (end < s.length) {
        if (set.has(s[end])) {
            set.delete(s[start])
            start++
        } else {
            set.add(s[end])
            maxLength = Math.max(maxLength, set.size)
            end++
        }
    }
    return maxLength
}

