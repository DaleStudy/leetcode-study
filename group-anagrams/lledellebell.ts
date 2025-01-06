/**
 * 
 * @problem
 * 문자열 배열이 주어졌을 때, 애너그램끼리 그룹화해야 합니다.
 *
 * (참고)
 * 애너그램(Anagram)이란 단어를 구성하는 문자의 순서를 바꿔서 다른 단어를 만드는 것을 의미합니다.
 * 예를 들어, "eat", "tea", "ate"는 모두 같은 문자로 구성되어 있으므로 애너그램입니다.
 *
 * @param {string[]} strs - 입력 문자열 배열
 * @returns {string[][]} 애너그램 그룹으로 묶인 2차원 문자열 배열
 *
 * @example
 * groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]); // [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
 * groupAnagrams([""]); // [[""]] 
 * groupAnagrams(["a"]); // [["a"]]
 *
 * @description
 * - 시간 복잡도: O(N * K log K)
 *   ㄴ N: 입력 문자열 배열의 길이
 *   ㄴ K: 각 문자열의 평균 길이
 *   각 문자열을 정렬하는 데 O(K log K)의 시간이 소요되며, 이를 N번 반복합니다.
 * - 공간 복잡도: O(N * K)
 *   해시맵에 저장되는 키와 값의 총 길이에 비례합니다.
 */
function groupAnagrams(strs: string[]): string[][] {
    // 애너그램 그룹을 저장할 해시맵
    const anagrams: Record<string, string[]> = {};

    // 입력 문자열 배열을 순회
    for (const str of strs) {
        // 문자열을 정렬하여 애너그램 그룹의 키 생성
        const key = str.split('').sort().join('');
        
        // 키가 해시맵에 없으면 초기화
        if (!anagrams[key]) {
            anagrams[key] = [];
        }

        // 해당 키에 문자열 추가
        anagrams[key].push(str);
    }

    // 해시맵의 값들만 반환 (애너그램 그룹)
    return Object.values(anagrams);
}

console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])); // [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
console.log(groupAnagrams([""])); // [[""]]
console.log(groupAnagrams(["a"])); // [["a"]]
