// Anagram - 두 문자열이 같은 알파벳을 같은 개수만큼 가지고 있어야 함.

// O(n log n) - 정렬 방식
const isAnagram = (s, t) => {
    // 1단계: 길이가 다르면 절대 anagram 불가 → 바로 false 반환
    if (s.length !== t.length) return false;

    // 2단계: 문자열을 배열로 쪼개고 → 정렬하고 → 다시 문자열로 합치기
    const sortedS = s.split('').sort().join('');
    const sortedT = t.split('').sort().join('');

    // 3단계: 정렬된 두 문자열이 같으면 anagram
    return sortedS === sortedT;
};

// O(n) - 해시맵 방식
const isAnagram2 = (s, t) => {
    // [주의] s.length는 실제 문자 수가 아닌 UTF-16 코드 유닛 수를 셈. - "The number of UTF-16 code units in the string"
    // 이모지 같은 문자는 코드 유닛 2개를 차지해서 실제 문자 수와 다를 수 있음.
    //   "😀".length  → 2  (코드 유닛 기준)
    //   [..."😀"].length → 1  (실제 문자 기준)
    // Unicode 완전 대응이 필요하면 [...s].length !== [...t].length 로 수정.
    // 이 문제는 소문자 영어 알파벳만 다루므로 s.length 사용해도 무방.
    if (s.length !== t.length) return false;

    const count = {};

    // for...of는 실제 문자 단위로 순회하므로 Unicode 안전.
    // count[char]가 없으면 0으로 초기화 후 +1.
    for (const char of s) {
        count[char] = (count[char] || 0) + 1;
    }

    // t에 있는 문자가 count에 없거나(0, undefined) → s에 없는 문자 → false.
    for (const char of t) {
        if (!count[char]) return false;
        count[char]--;
    }

    // 모든 문자가 소진되면 anagram.
    return true;
};
