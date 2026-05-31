/**
 * 문제: https://leetcode.com/problems/valid-anagram/description/
 *
 * 요구사항:
 * 두개의 문자열이 주어졌을 때 두개의 문자열이 애너그램인지 판단해서 boolean 으로 리턴
 *
 * * */

const validAnagram = (s, t) => {
    if(s.length !== t.length) return false;

    let count = {};

    for(const sChar of s) {
        count[sChar] = (count[sChar] || 0) + 1;
    }

    for(const tChar of t) {
        if(!count[tChar]) return false;
        count[tChar]--;
    }

    return true;
}
