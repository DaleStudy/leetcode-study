/**
 * 두 문자열이 애너그램인지 여부를 반환하는 함수
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const isAnagram = function (s, t) {
    if (s.length !== t.length) return false;

    const counter = Array.from(s).reduce((counter, char) => {
        counter[char] = counter[char] + 1 || 1;
        return counter;
    }, {});

    for (let char of t) {
        if (!counter[char] || counter[char] === 0) {
            return false;
        }

        counter[char] -= 1;
    }

    return true;
};

// 시간복잡도: O(n)
// 공간복잡도: O(n)
