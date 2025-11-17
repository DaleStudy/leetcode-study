/**
 * @param s 문자열 1
 * @param t 문자열 2
 * @returns 두 문자열의 나열을 바꿔 동일한 문자열이 나올 수 있는지 반환
 * @description
 * - 1. 시간 복잡도: O(n), 공간 복잡도 O(1)
 */

// function isAnagram(s: string, t: string): boolean {
//     if(s.length !== t.length) {
//         return false;
//     }
//     const sMap = new Map();
//     for(let i = 0; i < s.length; i++) {
//         sMap.has(s[i]) ? sMap.set(s[i], sMap.get(s[i]) + 1) : sMap.set(s[i], 1);
//         sMap.has(t[i]) ? sMap.set(t[i], sMap.get(t[i]) - 1) : sMap.set(t[i], -1);
//     }

//     for(const v of sMap.values()) {
//         if(v) {
//             return false;
//         }
//     }
//     return true;
// }

function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) return false;

    const hash: Record<string, number> = {};

    for (const letter of s) {
        hash[letter] = (hash[letter] || 0) + 1;
    }

    for (const letter of t) {
        if (hash[letter] > 0) {
            hash[letter] = hash[letter] - 1;
        } else {
            return false;
        }
    }

    return true;
}
