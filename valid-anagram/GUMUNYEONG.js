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

// TC : O(n)
// n(=s의 길이 = t의 길이) 만큼 반복 하므로 On(n)

// SC : O(n)
// 최대크기 n(=s의 길이 = t의 길이)만큼인 객체를 생성하므로 공간 복잡도도 O(n)
