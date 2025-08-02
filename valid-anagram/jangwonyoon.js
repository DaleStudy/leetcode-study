/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

/**
 * 유니크한 값만 확인한다.
 * 1. core: Map 사용하고, 모든 string을 할당한다.
 * 2. string을 순회해서 할당한다.
 * 3. map에 요소가 있으면 있으면 + 1, 없으면 1
 * 4. map을 순회해서 요소가 있다면 -1을 해준다.
 * 5. HashMap을 다시 한번 순회해서, 1이상 값이 있다면 유니크한 값이 아니기 때문에 false, HashMap의 모든 값들이 0이면 true

 * 공간복잡도 O(N)
 * 시간복잡도 O(N)
  */


var isAnagram = function(s, t) {
    const hashMap = new Map();

    // 예외 처리
    if (s.length !== t.length) {
        return false;
    }


    for (const string of s) {
        if (!hashMap.has(string)) {
            hashMap.set(string, 1)
        } else {
            hashMap.set(string, hashMap.get(string) + 1)
        }
    }

    for (const string of t) {
        if (hashMap.has(string)) {
            hashMap.set(string, hashMap.get(string) - 1);
        }
    }

    // 0이 아닌 값이 있는경우 - false
    for (const [key , value] of hashMap) {
        // early return
        if (value > 0) return false;
    }

    return true;
};
