/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const strsMap = new Map();
    for(let str of strs){
        const strArr = str.split('').sort()
        const keyName = strArr.join('-')
        strsMap.set(keyName,[...(strsMap.get(keyName)
        ||[]),str])
    }
    return Array.from(strsMap.values())
};

//시간복잡도 : O(n * klogk)
// 공간복잡도  :O(n · k)

//2.문자 빈도수 기반 키 만들기
// 알파벳이 26뿐이므로 각 단어마다 알파벳 개수를 세서 카운트배열 만들어 이걸 키로 사용
var groupAnagrams = function(strs) {
    const map = new Map();

    for (let str of strs) {
        const count = new Array(26).fill(0);
        for (let char of str) {
            count[char.charCodeAt(0) - 97]++;
        }
        const key = count.join('#'); // 구분자 없으면 ["1","11"]과 ["11","1"] 같은 키로 오해 가능
        map.set(key, [...(map.get(key) || []), str]);
    }

    return Array.from(map.values());
};

//시간복잡도 : O(n * k). 정렬이 없으므로
// 공간복잡도: O(n · k)
