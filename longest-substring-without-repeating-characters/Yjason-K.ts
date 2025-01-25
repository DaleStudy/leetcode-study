/**
 * 주어진 문자열에서 반복되지 않는 가장 긴 부분 문자열의 길이를 반환.
 * @param {sting} s - 주어진 문자열 
 * @returns {number} 주어진 문자열에서 중복 문자가 없는 가장 긴 부분 문자열의 길이
 * 
 * 시간 복잡도: O(n)
 * - 문자열 1회 순회
 * 
 * 공간 복잡도: O(n)
 * - 최대 문자열의 모든 문자를 Map에 저장하므로 입력 문자열의 길이에 비례하는 공간을 사용
 */
function lengthOfLongestSubstring(s: string): number {
    // 각 문자의 idx를 보관할 Map
    const charMap: Map<string, number> = new Map();

    // substring 최대 길이
    let maxLen = 0;
    // substring 시작점
    let start = 0;

    for (let end = 0; end < s.length; end++) {
        const char = s[end];

        // 문자가 이전에 등장했으며, 윈도우의 시작점(start)보다 크거나 같을 경우 업데이트
        const prevIdx = charMap.get(char);
        if (prevIdx && prevIdx >= start) {
            start = prevIdx + 1; // 중복 문자 이후로 윈도우의 시작점 이동
        }

        // 현재 문자의 위치 업데이트
        charMap.set(char, end);

        // 최대 길이 갱신
        maxLen = Math.max(maxLen, end - start + 1);

    } 

    return maxLen;
}

