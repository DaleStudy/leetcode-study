/**
 *
 * @param s
 * @param t
 *
 * 풀이 1
 * s.split("").sort().join("") === t.split("").sort().join("") ? true : false
 *
 * 시간 복잡도: O(n log n)
 * 공간 복잡도: O(n)
 *
 * 너무 비효율적임.. 문자열을 배열로 바꾸고 다시 배열로 변환하고.. 개선해보자
 *
 */

function isAnagram(s: string, t: string): boolean {
    if(s.length !== t.length) return false;

    // 해시맵 만들어주고
    const charCount : Record<string,number> = {};

    // 여기서는 늘려주고 O(n)
    for(let char of s){
        charCount[char] = (charCount[char] || 0) + 1;
    }

    // 여기는 존재하면 없애주자 O(n)
    for(let char of t){
        if(!charCount[char]) return false;
        charCount[char]--;
    }

    return true
};
