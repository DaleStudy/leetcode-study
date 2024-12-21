const getDictionary = (s) => {
    const arr = s.split('');

    const dict = {};

    for (let i=0; i<arr.length; i++) {
        const key = arr[i];
        const value = dict[key];

        if (value === undefined) {
            dict[key] = 1;
        } else {
            dict[key] = dict[key] + 1;
        }
    }

    return dict;
}

const checkSameLength = (dictA, dictB) => {
    return Object.keys(dictA).length === Object.keys(dictB).length
}

const checkSameDict = (s, t) => {
    for (const key in s) {
        if (s[key] !== t[key]) {
            return false;
        }
    }

    return true;
}

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    const dictA = getDictionary(s);

    const dictB = getDictionary(t);

    return checkSameLength(dictA, dictB) && checkSameDict(dictA, dictB);
};

// 공간복잡도: 해시 테이블에 모든 문자를 저장하게 되므로 O(n)
// 시간복잡도: 두 개의 문자열을 한 번씩 루프를 돌고 있기 때문에 0(n)

