/***
 * @problem
 * 주어진 문자열에서 중복되지 않는 문자로 이루어진 가장 긴 부분 문자열의 길이를 구해야 합니다.
 * 
 * @constraints
 * - 문자열의 길이는 0 이상 5 * 10^4 이하입니다.
 * - 문자열은 ASCII 문자로만 구성됩니다.
 * 
 * @example
 * - 입력: "abcabcbb"
 *   출력: 3 ("abc")
 * - 입력: "bbbbb"
 *   출력: 1 ("b")
 * - 입력: "pwwkew"
 *   출력: 3 ("wke")
 * 
 * @description
 * - ASCII 문자의 마지막 위치를 저장할 배열을 사용합니다.
 * - 중복 문자가 발견되면 시작 지점을 해당 문자의 마지막 위치 다음으로 이동합니다.
 * - 현재 서브스트링의 길이를 계산하여 최대 길이를 갱신합니다.
 * 
 * @complexity
 * - 시간 복잡도: O(n)
 *   ㄴ 문자열을 한 번 순회하며 각 문자를 처리합니다.
 * - 공간 복잡도: O(1)
 *   ㄴ 고정 크기 배열(128)을 사용하므로 공간 복잡도는 상수입니다.
 */
function lengthOfLongestSubstring(s: string): number {
    // ASCII 문자의 마지막 위치를 저장할 배열 (128 크기, 초기값 -1)
    const lastSeenIndex = Array(128).fill(-1);
    let substringStart = 0;
    let longestLength = 0;

    for (let currentIndex = 0; currentIndex < s.length; currentIndex++) {
        const currentCharCode = s.charCodeAt(currentIndex);

        // 중복 문자가 발견되었고, 그 문자의 마지막 위치가 현재 시작점 이후라면
        if (lastSeenIndex[currentCharCode] >= substringStart) {
            // 시작 지점을 중복 문자의 다음 위치로 이동
            substringStart = lastSeenIndex[currentCharCode] + 1;
        }

        // 현재 문자의 위치를 배열에 저장
        lastSeenIndex[currentCharCode] = currentIndex;

        // 현재 서브스트링의 길이를 계산하고 최대값 갱신
        longestLength = Math.max(longestLength, currentIndex - substringStart + 1);
    }

    return longestLength;
}

// 테스트
console.log(lengthOfLongestSubstring("abcabcbb")); // 출력: 3
console.log(lengthOfLongestSubstring("bbbbb"));    // 출력: 1
console.log(lengthOfLongestSubstring("pwwkew"));   // 출력: 3
