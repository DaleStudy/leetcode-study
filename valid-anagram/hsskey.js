/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(s.length !== t.length) {
        return false
    }
    const sMap = new Map()
    const tMap = new Map()

    for(let i = 0; i < s.length; i++) {
        if(sMap.has(s[i])) {
            const prevVal = sMap.get(s[i])
            sMap.set(s[i], prevVal + 1)
        } else {
            sMap.set(s[i], 1)
        }
    }

    for(let i = 0; i < t.length; i++) {
        if(tMap.has(t[i])) {
            const prevVal = tMap.get(t[i])
            tMap.set(t[i], prevVal + 1)
        } else {
            tMap.set(t[i], 1)
        }
    }

    for(const[char, count] of sMap) {
        if(!tMap.has(char) || tMap.get(char) !== count) {
            return false
        }
    }

    return true
};
