// https://leetcode.com/problems/valid-anagram/submissions/1603502655/

// TC: O(NlogN)
// SC: O(N)

var isAnagram = function (s, t) {
    return s.split("").sort().join("") === t.split("").sort().join("")
};

// TC: O(N)
// SC: O(N)

var isAnagram = function (s, t) {
    const map = new Map()

    for (const char of s) {
        if (map.has(char)) map.set(char, map.get(char) + 1)
        else map.set(char, 1)
    }

    for (const char of t) {
        if (!map.has(char)) return false
        else map.set(char, map.get(char) - 1)
    }

    for (const value of map.values()) {
        if (value !== 0) return false
    }

    return true
};

console.log(isAnagram(s = "anagram", t = "nagaram"))