/**
 * 두 문자열을 비교해서 Anagram 여부 확인
 * - 시간 복잡도: O(n)
 *   - 문자열 순회와 비교 과정을 포함하여 n은 문자열의 길이
 * - 공간 복잡도: 0(1)
 *   - 알파벳 개수가 26개로 고정 상수 공간
 * @param {string} s - 문자열 s 
 * @param {string} t - 문자열 t
 * @returns {boolean} - Anagram 여부
 */
function isAnagram(s: string, t: string): boolean {
    // 두 문열의 길이가 다른경우 false 반환
    if (s.length !== t.length) {
        return false;
    }

    // 문자열 알파벳 사전을 위한 객체 선언
    let vocabS = {};
    let vocabT = {};

    // s 문자열에 대한 알파벳 사전 생성
    for (const char in s) {
        vocabS = vocabS[char] ? vocabS[char] + 1 : 1;
    };

    // t 문자열에 대한 알파벳 사전 생성
    for (const char in t) {
        vocabT = vocabT[char] ? vocabT[char] + 1 : 1;


    // 두 문자열 사전을 비교하며 count 가 일치 하지 않은 경우 false 반환
    for (const char in vocabS) {
        if (vocabS[char] !== vocabT[char]) {
            return false;
        }
    }

    return true;
};

