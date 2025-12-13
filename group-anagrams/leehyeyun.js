/**
 * @param {string[]} strs
 * @return {string[][]}
 */
/*
주어진 문자열 배열 strs에서,
서로 아나그램(anagram) 관계인 문자열들을 묶어 그룹으로 반환하는 문제이다.

아나그램이란?
  - 문자열의 문자들을 재배열하여 서로 같은 구성을 만들 수 있는 문자열을 의미한다.
  - 예: "eat", "tea", "ate"는 같은 아나그램 그룹에 속함.

목표:
  - strs 내 모든 문자열을 아나그램끼리 묶은 그룹들의 배열로 반환한다.
  - 그룹의 순서나, 그룹 내부 문자열의 순서는 중요하지 않다.

입력 형식 :
  - strs: 문자열 배열
  - 1 <= strs.length <= 10,000
  - 0 <= strs[i].length <= 100
  - strs[i]는 모두 소문자 영어 알파벳으로 구성됨

출력 형식 :
  - 아나그램끼리 묶인 그룹들의 배열 (2차원 배열)

예시 :

  Example 1
    입력 : ["eat","tea","tan","ate","nat","bat"]
    출력 : [["bat"], ["nat","tan"], ["ate","eat","tea"]]
    설명 :
      - "eat", "tea", "ate"는 문자 구성이 동일하므로 같은 그룹
      - "tan", "nat"도 서로 아나그램이므로 같은 그룹
      - "bat"는 다른 어떤 문자열로도 아나그램을 만들 수 없으므로 단독 그룹

  Example 2
    입력 : [""]
    출력 : [[""]]
    설명 :
      - 빈 문자열도 하나의 문자열로 취급되며, 자신과 함께 단일 그룹 생성

  Example 3
    입력 : ["a"]
    출력 : [["a"]]
    설명 :
      - 단일 문자 하나만 있으므로 그대로 그룹화됨
*/
var groupAnagrams = function (strs) {

    const processed = new Set();
    const result = [];

    for (let i = 0; i < strs.length; i++) {

        const base_word = strs[i];
        if (processed.has(base_word)) continue;

        const baseMap = new Map();

        for (const base_word_char of base_word) {
            if (baseMap.has(base_word_char)) {
                let base_word_char_count = baseMap.get(base_word_char);

                base_word_char_count++;
                baseMap.set(base_word_char, base_word_char_count)
            } else {
                baseMap.set(base_word_char, 1)
            }
        }

        const group = [base_word];
        processed.add(base_word);

        for (let j = i + 1; j < strs.length; j++) {

            const candidate_word = strs[j];

            if (processed.has(candidate_word)) continue;

            const compareMap = new Map([...baseMap]);

            for (const candidate_word_char of candidate_word) {
                if (compareMap.has(candidate_word_char)) {

                    let candidate_word_char_count = compareMap.get(candidate_word_char)
                    candidate_word_char_count--;

                    if (candidate_word_char_count === 0) {
                        compareMap.delete(candidate_word_char)
                    } else if (candidate_word_char_count > 0) {
                        compareMap.set(candidate_word_char, candidate_word_char_count)
                    }
                }
            }

            //최종 리턴
            if (compareMap.size == 0) {
                processed.add(candidate_word);
                group.push(candidate_word);
            }
        }

        result.push(group);

    }

    return result;
};

console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
console.log(groupAnagrams([""]))
console.log(groupAnagrams(["a"]))


