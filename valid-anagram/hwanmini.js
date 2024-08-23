// 시간복잡도: O(n)
// 공간복잡도: O(k)

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) return false

    const checkMap = new Map();

    for (let i = 0; i < s.length; i++) {
        checkMap.set(s[i], (checkMap.get(s[i]) || 0) + 1)
    }


    for (let j = 0; j < t.length; j++) {
        if (!checkMap.get(t[j]) || checkMap.get(t[j]) < 0) return false
        checkMap.set(t[j], (checkMap.get(t[j]) || 0 ) - 1);
    }

    return true
};


console.log(isAnagram("anagram","nagaram"))