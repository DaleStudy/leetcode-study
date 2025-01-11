/**
 * 애너그램 그룹화하기
 * n - 입력 문자열 배열의 길이
 * k - 가장 긴 문자열의 길이
 *
 * 알고리즘 복잡도
 * - 시간 복잡도: n * k * logk (sort가 klogk 시간 소요)
 * - 공간 복잡도: n * k
 * @param strs
 */
function groupAnagrams(strs: string[]): string[][] {
    let group = {}

    for(const s of strs) {
        let key = s.split('').sort().join('');
        if(!group[key]) {
            group[key] = []
        }
        group[key].push(s)
    }
    console.log(group)

    return Object.values(group)
}
