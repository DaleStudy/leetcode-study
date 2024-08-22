/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
    const countHash = {};
    let result = true;

    if (s.length !== t.length) return false;

    for (str_t of t) {
        countHash[str_t] ? countHash[str_t]++ : countHash[str_t] = 1;
    }

    for (str_s of s) {
        if (countHash[str_s]) {
            countHash[str_s]--;
        } else {
            result = false;
            break;
        }
    }

    return result;
};
