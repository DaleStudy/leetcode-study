/**
 * 주어진 문자열 배열에서 Anagram을 그룹화 해서 배열 만들기
 * @param {string[]} strs - 문자열 배열
 * @returns {string[][]} Anagram을 그룹 배열
 * 
 * 문자열들을 정렬해서 Map에 담아서 존재하면 그 때의 문자를 value로 추가
 * 존재하지 않으면 새로운 배열을 value로 추가
 * 
 * 시간 복잡도: O(N * M * log(M))
 *  - N은 문자열 배열의 길이
 *  - M은 각 문자열의 평균 길이 (정렬 시간 때문)
 * 공간 복잡도: O(N * M)
 *  - 해시맵에 저장되는 문자열 그룹 때문
 */
function groupAnagrams(strs: string[]): string[][] {
    const anagramMap: Map<string, string[]> = new Map();
    for (const str of strs) {

        // 정렬된 문자열
        const sortedStr = str.split('').sort().join('');

        // 정렬된 문자열이 존재하는 않는 경우
        if (!anagramMap.has(sortedStr)) {
            anagramMap.set(sortedStr, [])
        }

        // 정렬된 문자열을 key로 하는 value str 추가
        anagramMap.get(sortedStr)?.push(str);
    }

    // anagramMap에서 values만 배열로해서 출력
    return Array.from(anagramMap.values())
}